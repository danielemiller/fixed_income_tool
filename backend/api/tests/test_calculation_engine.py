# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.config.settings')
# from django.conf import settings
# settings.configure()

# backend/api/tests/test_calculation_engine.py
import pytest
import math
from api.calculation_engine import (
    bond_price, yield_to_maturity, yield_to_call, average_life, duration, convexity, credit_spread, option_adjusted_spread, calculate_bond_metrics
)

@pytest.fixture
def parsed_data():
    return {
        'face_value': 1000,
        'coupon_rate': 0.05,
        'yield_to_maturity': 0.06,
        'years_to_maturity': 5,
        'years_to_call': 3,
        'call_price': 1010,
        'payment_schedule': [50, 50, 50, 50, 1050],
        'risk_free_yield': 0.04,
        'benchmark_yield': 0.05,
        'option_value': 0.01
    }

def test_bond_price(parsed_data):
    assert math.isclose(bond_price(parsed_data['face_value'], parsed_data['coupon_rate'], parsed_data['yield_to_maturity'], parsed_data['years_to_maturity']), 950.388, rel_tol=1e-5)

def test_yield_to_maturity(parsed_data):
    bond_price_val = bond_price(parsed_data['face_value'], parsed_data['coupon_rate'], parsed_data['yield_to_maturity'], parsed_data['years_to_maturity'])
    assert math.isclose(yield_to_maturity(bond_price_val, parsed_data['face_value'], parsed_data['coupon_rate'], parsed_data['years_to_maturity']), 0.06, rel_tol=1e-5)

def test_yield_to_call(parsed_data):
    bond_price_val = bond_price(parsed_data['face_value'], parsed_data['coupon_rate'], parsed_data['yield_to_maturity'], parsed_data['years_to_maturity'])
    assert math.isclose(yield_to_call(bond_price_val, parsed_data['face_value'], parsed_data['coupon_rate'], parsed_data['years_to_call'], parsed_data['call_price']), 0.07172050769272936, rel_tol=1e-3)

def test_average_life(parsed_data):
    assert math.isclose(average_life(parsed_data['payment_schedule']), 4.6, rel_tol=1e-5)

def test_duration(parsed_data):
    assert math.isclose(duration(parsed_data['face_value'], parsed_data['coupon_rate'], parsed_data['yield_to_maturity'], parsed_data['years_to_maturity']), 4.570, rel_tol=1e-4)

def test_convexity(parsed_data):
    assert math.isclose(convexity(parsed_data['face_value'], parsed_data['coupon_rate'], parsed_data['yield_to_maturity'], parsed_data['years_to_maturity']), 23.595, rel_tol=1e-5)

def test_credit_spread(parsed_data):
    assert round(credit_spread(parsed_data['yield_to_maturity'], parsed_data['risk_free_yield']), 2) == 0.02

def test_option_adjusted_spread(parsed_data):
    assert math.isclose(option_adjusted_spread(parsed_data['yield_to_maturity'], parsed_data['benchmark_yield'], parsed_data['option_value']), -5.204170427930421e-18, rel_tol=1e-3)

def test_calculate_bond_metrics(parsed_data):
    bond_metrics = calculate_bond_metrics(parsed_data)
    assert math.isclose(bond_metrics['bond_price'], 950.388, rel_tol=1e-5)
    assert math.isclose(bond_metrics['yield_to_maturity'], 0.06, rel_tol=1e-5)
    assert math.isclose(bond_metrics['yield_to_call'], 0.07172050769272936, rel_tol=1e-3)
    assert math.isclose(bond_metrics['average_life'], 4.6, rel_tol=1e-5)
    assert math.isclose(bond_metrics['duration'], 4.570, rel_tol=1e-4)
    assert math.isclose(bond_metrics['convexity'], 23.595, rel_tol=1e-5)
    assert round(bond_metrics['credit_spread'], 2) == 0.02
    assert math.isclose(bond_metrics['option_adjusted_spread'], -5.204170427930421e-18, rel_tol=1e-3)