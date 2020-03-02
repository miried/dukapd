from . import constants

instrument_type = None
instrument_name = None

def log_output(s, loglevel):
    """Print log message if loglevel is high enough."""
    if loglevel > constants.LOGLEVEL:
        print(s)

def get_filepath(instrument, date, hour):
    """File path for instrument as found on Dukascopy server."""
    datestring = '{:04d}/{:02d}/{:02d}'.format(date.year,date.month-1,date.day)
    s = '{}/{}/{:02d}h_ticks.bi5'.format(instrument, datestring, hour)
    return s
