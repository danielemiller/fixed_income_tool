# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.config.settings')
# from django.conf import settings
# settings.configure()

# backend/api/tests/test_external_data.py
import pytest
from api.external_data import get_bond_price, get_risk_free_yield, get_benchmark_yield


def test_get_bond_price(mocker):
    mock_data = {
        '2023-04-07': {'4. close': '105.25'}
    }
    mocker.patch('api.external_data.ts.get_daily', return_value=(mock_data, {}))

    bond_price = get_bond_price('TEST_BOND')
    assert bond_price == 105.25

def test_get_risk_free_yield(mocker):
    mocker.patch('api.external_data.fred.get_series', return_value=[1.5])

    risk_free_yield = get_risk_free_yield()
    assert risk_free_yield == 0.015

def test_get_benchmark_yield(mocker):
    mocker.patch('api.external_data.fred.get_series', return_value=[2.0])

    benchmark_yield = get_benchmark_yield()
    assert benchmark_yield == 0.02
