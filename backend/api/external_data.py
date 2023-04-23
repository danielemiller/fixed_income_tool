import os
import requests
from fredapi import Fred

try:
    from config import FRED_API_KEY
except ImportError:
    FRED_API_KEY = os.environ['FRED_API_KEY']

fred = Fred(api_key=FRED_API_KEY)

try:
    from config import FASTTRACK_APP_ID, FASTTRACK_ACCOUNT_NUMBER, FASTTRACK_PASSWORD
except ImportError:
    FASTTRACK_APP_ID = os.environ['FASTTRACK_APP_ID']
    FASTTRACK_ACCOUNT_NUMBER = os.environ['FASTTRACK_ACCOUNT_NUMBER']
    FASTTRACK_PASSWORD = os.environ['FASTTRACK_PASSWORD']

APP_ID = FASTTRACK_APP_ID
ACCOUNT_NUMBER = FASTTRACK_ACCOUNT_NUMBER
PASSWORD = FASTTRACK_PASSWORD

def authenticate():
    url = "https://ftl.fasttrack.net/v1/auth/login"
    headers = {"Content-Type": "application/json"}
    params = {
        "account": ACCOUNT_NUMBER,
        "appid": APP_ID,
        "pass": PASSWORD,
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print("Authentication response content:", response.content)
    response.raise_for_status()
    data = response.json()

    if 'token' not in data:
        raise ValueError("Authentication failed. Please check your credentials in the config file or environment variables.")

    return data['token']


def get_bond_data(cusip, start_date=None, end_date=None):
    token = authenticate()
    url = f'https://ftl.fasttrack.net/v1/bonds/{cusip}/data'
    print(f"url={url}")
    headers = {
        'appid': APP_ID,
        'token': token
    }
    params = {}
    if start_date:
        params['start'] = start_date
    if end_date:
        params['end'] = end_date

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching bond data for CUSIP {cusip}: {response.status_code}")
        return None

def get_bond_price(cusip, start_date=None, end_date=None):
    bond_data = get_bond_data(cusip, start_date, end_date)
    if bond_data:
        bond_price = bond_data['prices'][-1]['price']
        return bond_price
    else:
        return None

def get_risk_free_yield():
    risk_free_yield = float(fred.get_series('GS10')[-1]) / 100  # 10-Year Treasury Constant Maturity Rate
    return risk_free_yield

def get_benchmark_yield():
    benchmark_yield = float(fred.get_series('GS10')[-1]) / 100  # 10-Year Treasury Constant Maturity Rate
    return benchmark_yield

def get_yield_data(series_id):
    return float(fred.get_series(series_id)[-1]) / 100

SERIES_IDS = {
    1: 'GS1M',   # 1-month Treasury Constant Maturity Rate
    3: 'GS3M',   # 3-month Treasury Constant Maturity Rate
    6: 'GS6M',   # 6-month Treasury Constant Maturity Rate
    1: 'GS1',    # 1-year Treasury Constant Maturity Rate
    2: 'GS2',    # 2-year Treasury Constant Maturity Rate
    3: 'GS3',    # 3-year Treasury Constant Maturity Rate
    5: 'GS5',    # 5-year Treasury Constant Maturity Rate
    7: 'GS7',    # 7-year Treasury Constant Maturity Rate
    10: 'GS10',  # 10-year Treasury Constant Maturity Rate
    20: 'GS20',  # 20-year Treasury Constant Maturity Rate
    30: 'GS30'   # 30-year Treasury Constant Maturity Rate
}

def get_bond_data_list(face_value=1000, coupon_rate=0.0):
    bond_data_list = []
    for maturity, series_id in SERIES_IDS.items():
        yield_data = get_yield_data(series_id)
        price = face_value * (1 + yield_data)
        maturity_years = float(maturity.rstrip('MY'))
        bond_data = {
            'coupon_rate': coupon_rate,
            'face_value': face_value,
            'price': price,
            'maturity': maturity_years
        }
        bond_data_list.append(bond_data)
    return bond_data_list
