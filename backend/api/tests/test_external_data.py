# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.config.settings')
# from django.conf import settings
# settings.configure()

# backend/api/tests/test_external_data.py
import pytest
from unittest.mock import MagicMock, patch
from ..external_data import fetch_market_data

def test_fetch_market_data():
    # Mock the API response
    mock_api_response = {
        'status': 'success',
        'data': {
            'timestamp': 1620133200,
            'yield_curve': [
                {'maturity': '1M', 'rate': 0.01},
                {'maturity': '3M', 'rate': 0.02},
                {'maturity': '6M', 'rate': 0.03},
                # ...
            ],
        },
    }

    with patch('requests.get') as mock_get:
        # Replace the real API call with our mock API response
        mock_get.return_value = MagicMock(json=lambda: mock_api_response)

        # Call the function that fetches market data
        market_data = fetch_market_data()

        # Assert that the data is correctly retrieved and processed
        assert market_data['yield_curve'] == [
            {'maturity': '1M', 'rate': 0.01},
            {'maturity': '3M', 'rate': 0.02},
            {'maturity': '6M', 'rate': 0.03},
            # ...
        ]
