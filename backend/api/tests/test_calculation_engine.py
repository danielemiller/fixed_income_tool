# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.config.settings')
# from django.conf import settings
# settings.configure()

# backend/api/tests/test_calculation_engine.py
import pytest
from ..calculation_engine import bond_price, yield_to_maturity

def test_bond_price():
    face_value = 1000
    coupon_rate = 0.05
    yield_to_maturity = 0.04
    years_to_maturity = 10
    expected_price = 1043.76

    calculated_price = bond_price(face_value, coupon_rate, yield_to_maturity, years_to_maturity)

    assert pytest.approx(calculated_price, 0.01) == expected_price

def test_yield_to_maturity():
    bond_price = 1043.76
    face_value = 1000
    coupon_rate = 0.05
    years_to_maturity = 10
    expected_yield = 0.04

    calculated_yield = yield_to_maturity(bond_price, face_value, coupon_rate, years_to_maturity)

    assert pytest.approx(calculated_yield, 0.0001) == expected_yield
