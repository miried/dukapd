from . import constants
from . import helpers

import os
import time
import datetime
from subprocess import Popen, PIPE

import numpy as np
import pandas as pd


UINT32  = np.dtype(np.uint32)
FLOAT32 = np.dtype(np.float32)

def decompress_bi5(filename):
    """Use lzma to decompress the bi5 file."""
    if os.path.getsize(filename) == 0:
        result = b''
    else:
        proc = Popen(['lzma', '--decompress', '--stdout', filename], stdout=PIPE, stderr=PIPE)
        out, err = proc.communicate()
        exitcode = proc.returncode
        if exitcode != 0:
            raise Exception(err.decode())
        result = out
    return result

def bi5_to_dataframe(filepath):
    """Convert the bi5 file to a Pandas DataFrame."""
    #fmt = '>3i2f'
    filename = constants.OUT_DIR + filepath
    
    try:
        uncompressed = decompress_bi5(filename)
        
        raw_be   = np.frombuffer(uncompressed, dtype=UINT32).reshape(-1,5)
        raw_le   = raw_be.byteswap()
        int_data = raw_le[:,0:3]
        flt_data = raw_le[:,3:5].view(dtype=FLOAT32)
        
        data = {
            'Timestamp' : int_data[:,0],
            'Ask'       : int_data[:,1],
            'Bid'       : int_data[:,2],
            'AskVolume' : flt_data[:,0],
            'BidVolume' : flt_data[:,1]
        }
    except:
        print('Problem reading file {}'.format(filename))
        raise
    if True:
        df = pd.DataFrame(data)
    else:
        df = None
    return df

def convert_ticks(start_date, end_date, instr_type=None, instr_name=None):
    """Convert the downloaded files to a Pandas DataFrame."""
    if instr_type is None:
        instr_type=helpers.instrument_type
    if instr_name is None:
        instr_name=helpers.instrument_name
    instrument = constants.INSTRUMENTS[instr_type][instr_name]

    hourly_results = []

    t_start = time.perf_counter()

    date = start_date
    while date <= end_date:
        for hour in range(24):
            dt_hour  = date + datetime.timedelta(hours=hour)
            filepath = helpers.get_filepath(instrument, date, hour)
            raw_df   = bi5_to_dataframe(filepath)

            if raw_df is not None:
                raw_df['Timestamp'] = raw_df['Timestamp'].map( lambda t : dt_hour + datetime.timedelta(milliseconds=t) )
                hourly_results.append(raw_df)

        if date.day == 1 and not date.month % 4:
            helpers.log_output('Completed {}'.format(date), 3)
        date += datetime.timedelta(days=1)

    df = pd.concat(hourly_results, ignore_index=True)

    time_elapsed = time.perf_counter() - t_start
    helpers.log_output('took {:.1f} s'.format(time_elapsed), 3)
    
    return df