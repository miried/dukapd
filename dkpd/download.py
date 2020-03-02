from . import constants
from . import helpers

import os
import time
import datetime
import requests


def download_file(baseurl, filepath, session):
    """Download from Dukascopy server."""
    in_url       = baseurl + filepath
    out_filepath = constants.OUT_DIR + filepath
    dirname      = os.path.dirname(out_filepath)
    
    os.makedirs(dirname, exist_ok=True)
    
    helpers.log_output('downloading {}'.format(in_url), 2)
    r = session.get(in_url, stream=True)
    
    if r.status_code == requests.status_codes.codes.OK:
        with open(out_filepath, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
        helpers.log_output('wrote to {}'.format(out_filepath), 1)
    else:
        raise Exception('Could not download {}.\nStatus code {}: {}'.format(
            in_url, r.status_code, requests.status_codes._codes[r.status_code]))


def download_ticks(start_date, end_date, instr_type=None, instr_name=None, rate_limit=constants.RATELIMIT ):
    """Download the ticks."""
    time_per_request = 1/rate_limit
    
    if instr_type is None:
        instr_type=helpers.instrument_type
    if instr_name is None:
        instr_name=helpers.instrument_name
    instrument = constants.INSTRUMENTS[instr_type][instr_name]

    with requests.Session() as s:
        date               = start_date
        t_start            = time.perf_counter()
        requests_completed = 0
        days_completed     = 0

        try:
            while date <= end_date:
                for hour in range(24):
                    filepath = helpers.get_filepath(instrument, date, hour)
                    download_file(constants.BASE_URL, filepath, s)
                    time_elapsed = time.perf_counter() - t_start
                    requests_completed += 1
                    time_min_allowed = requests_completed * time_per_request
                    time_excess      = time_min_allowed - time_elapsed
                    if time_excess > 0:
                        time.sleep(time_excess)
                if date.day == 1:
                    helpers.log_output('Completed {}'.format(date), 3)
                date += datetime.timedelta(days=1)
                days_completed += 1
        except:
            print('Exception on day {}'.format(date))
            raise
        finally:
            helpers.log_output(instrument, 4)
            msg = '{} requests for {} days in {:.1f} s'.format(requests_completed, days_completed, time_elapsed)
            helpers.log_output(msg, 4)
            if days_completed > 0:
                helpers.log_output('requests per day {}'.format(requests_completed/days_completed), 4)
            helpers.log_output('Request rate: {:.1f} / s'.format(requests_completed / time_elapsed), 4)