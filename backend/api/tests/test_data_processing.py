# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.config.settings')
# from django.conf import settings
# settings.configure()

# backend/api/tests/test_data_processing.py
from datetime import date, datetime
import pytest
from api.data_processing import parse_date, format_output_data

def test_parse_date():
    date_string = '2020-01-01'
    expected_date = date(2020, 1, 1)
    assert parse_date(date_string) == expected_date

def test_format_output_data():
    output_data = {
        'bond_price': 1043.76,
        'yield_to_maturity': 0.04,
    }
    expected_output = {
        'bond_price': '1,043.76',
        'yield_to_maturity': '4.00%',
        'fetched_bond_price': '1,043.76',  # Add the fetched_bond_price key with the appropriate formatted value
    }

    fetched_bond_price = 1043.76  # Add an appropriate value for the fetched_bond_price argument

    formatted_output = format_output_data(output_data, fetched_bond_price)

    assert formatted_output == expected_output