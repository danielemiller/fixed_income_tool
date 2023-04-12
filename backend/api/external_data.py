import requests
import os
from alpha_vantage.timeseries import TimeSeries
from fredapi import Fred

try:
    from config import ALPHA_VANTAGE_API_KEY, FRED_API_KEY
except ImportError:
    ALPHA_VANTAGE_API_KEY = os.environ['ALPHA_VANTAGE_API_KEY']
    FRED_API_KEY = os.environ['FRED_API_KEY']


ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY)
fred = Fred(api_key=FRED_API_KEY)

def get_bond_price(symbol):
    data, _ = ts.get_daily(symbol=symbol, outputsize='compact')
    bond_price = float(data[list(data.keys())[-1]]['4. close'])
    return bond_price

def get_risk_free_yield():
    risk_free_yield = float(fred.get_series('GS10')[-1]) / 100  # 10-Year Treasury Constant Maturity Rate
    return risk_free_yield

def get_benchmark_yield():
    benchmark_yield = float(fred.get_series('GS10')[-1]) / 100  # 10-Year Treasury Constant Maturity Rate
    return benchmark_yield
