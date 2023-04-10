# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.config.settings')
# from django.conf import settings
# settings.configure()

# backend/api/tests/test_endpoints.py
from typing import Any
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from api.models import BondData
from .factories import BondDataFactory

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def test_data():
    return {
    "face_value": 1000,
    "coupon_rate": 5.0,
    "yield_to_maturity": 5.5,
    "years_to_maturity": 10,
    "credit_rating": "AAA",
    "currency": "USD",
    "issue_date": "2020-01-01",
    "call_price": 1050,
    "years_to_call": 5,
    'maturity_date': '2026-03-01',
    "issuer": "Mock Issuer",
    'payment_schedule': [
        {'period': 1, 'payment': 50},
        {'period': 2, 'payment': 50},
        {'period': 3, 'payment': 50},
        {'period': 4, 'payment': 50},
        {'period': 5, 'payment': 1050},
    ],
    'risk_free_yield': 0.04,
    'benchmark_yield': 0.05,
    'option_value': 0.01
}

        

def test_process_bond_data(api_client: APIClient, test_data: dict[str, Any]):
    url = reverse('api:process_bond_data')  # Assuming you have a named URL 'process_bond_data'
    response = api_client.post(url, test_data, format='json')

    assert response.status_code == 200
    # You can also assert the response data, depending on your API implementation  
