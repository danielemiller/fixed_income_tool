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
        'issue_date': '2020-01-01',
        'maturity_date': '2030-01-01',
        'coupon_rate': 5.0,
        'yield_to_maturity': 4.0,
        'credit_rating': 'AAA',
        'currency': 'USD',
        'issuer': 'Test Issuer',
    }

def test_process_bond_data(api_client: APIClient, test_data: dict[str, Any]):
    url = reverse('api:process_bond_data')  # Assuming you have a named URL 'process_bond_data'
    response = api_client.post(url, test_data, format='json')

    assert response.status_code == 200
    # You can also assert the response data, depending on your API implementation  
