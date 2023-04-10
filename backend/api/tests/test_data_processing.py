# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.config.settings')
# from django.conf import settings
# settings.configure()

# backend/api/tests/test_data_processing.py
from datetime import date, datetime
import pytest
from api.data_processing import parse_date, format_output_data

# def test_parse_date():
#     date_string = '2020-01-01'
#     expected_date = datetime.date(2020, 1, 1)

#     parsed_date = parse_date(date_string)

#     assert parsed_date == expected_date
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
    }

    formatted_output = format_output_data(output_data)

    assert formatted_output == expected_output