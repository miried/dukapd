# The URL where to get the data from
BASE_URL  = 'https://datafeed.dukascopy.com/datafeed/'
# Maximum number of requests per second
RATELIMIT = 10

# Where to save the downloaded data.
OUT_DIR = 'data/'

# After which level to log.
LOGLEVEL = 2

BONDS = {
    'bund'   : 'BUNDTREUR',
    'gilt'   : 'UKGILTTRGBP'
}

INDICES = {
    'smi'    : 'CHEIDXEUR',
    'dax'    : 'DEUIDXEUR',
    'cac'    : 'FRAIDXEUR',
    'ftse'   : 'GBRIDXGBP',
    'aex'    : 'NLDIDXEUR',
    'sx5e'   : 'EUSIDXEUR',
    'spx'    : 'USA500IDXUSD',
    'dji'    : 'USA30IDXUSD',
    'nasdaq' : 'USATECHIDXUSD',
    'nikkei' : 'JPNIDXJPY',
    'hsi'    : 'HKGIDXHKD',
    'china50': 'CHIIDXUSD'
}

CURRENCIES = {
    'EURUSD' : 'EURUSD',
    'EURCHF' : 'EURCHF'
}

METALS = {
    'gold'   : 'XAUUSD',
    'silver' : 'XAGUSD',
    'copper' : 'COPPERCMDUSD'
}

ENERGY = {
    'brent'  : 'BRENTCMDUSD',
    'light'  : 'LIGHTCMDUSD',
    'diesel' : 'DIESELCMDUSD',
    'gas'    : 'GASCMDUSD'
}

AGRICULTURE = {
    'cocoa'  : 'COCOACMDUSD',
    'coffee' : 'COFFEECMDUSD',
    'cotton' : 'COTTONCMDUSD',
    'ojuice' : 'OJUICECMDUSD',
    'sugar'  : 'SUGARCMDUSD'
}

ETF = {
    'treasury' : 'IEFUSUSD',
    'vix'      : 'VXXUSUSD'
}

INSTRUMENTS = {
    'bonds' : BONDS, 'indices' : INDICES, 'currencies' : CURRENCIES,
    'metals' : METALS, 'energy' : ENERGY, 'agriculture' : AGRICULTURE, 'etf' : ETF
}

