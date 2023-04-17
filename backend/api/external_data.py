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
    print(f"ACCOUNT_NUMBER={ACCOUNT_NUMBER}")
    print(f"APP_ID={APP_ID}")
    print(f"PASSWORD={PASSWORD}")
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
