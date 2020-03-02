from .download import download_ticks
from .convert import convert_ticks
from .helpers import instrument_type, instrument_name
from .constants import INSTRUMENTS

def get_instrument():
    """Get the current instrument"""
    return INSTRUMENTS[helpers.instrument_type][helpers.instrument_name]

def set_instrument(instr_type, instr_name):
    """Set the default instrument."""
    helpers.instrument_name = instr_name
    helpers.instrument_type = instr_type
