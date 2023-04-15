# data_storage/db/tests/conftest.py
import pytest
from backend.api.models import BondData, ValuationMetrics, RiskAnalysisMetrics, HistoricalData
from datetime import date

@pytest.fixture
def bond(db):
    bond_instance = BondData.objects.create(
        name="Test Bond",
        issuer="Test Issuer",
        face_value=1000.00,
        coupon_rate=5.00,
        maturity_date=date(2030, 12, 31),
        credit_rating="A"
    )
    return bond_instance

@pytest.fixture
def valuation_metrics(db, bond):
    valuation_metrics_instance = ValuationMetrics.objects.create(
        bond=bond,
        bond_price=1010.00,
        yield_to_maturity=4.90,
        modified_duration=8.00,
        macaulay_duration=8.10,
        convexity=85.00,
        credit_spread=1.00
    )
    return valuation_metrics_instance

@pytest.fixture
def risk_analysis_metrics(db, bond):
    risk_analysis_metrics_instance = RiskAnalysisMetrics.objects.create(
        bond=bond,
        yield_to_call=4.80,
        average_life=7.50,
        option_adjusted_spread=0.50,
        risk_free_yield=4.00
    )
    return risk_analysis_metrics_instance

@pytest.fixture
def historical_data(db, bond):
    historical_data_instance = HistoricalData.objects.create(
        bond=bond,
        date=date(2020, 1, 1),
        price=1005.00,
        yield_to_maturity=5.10,
        credit_spread=1.10
    )
    return historical_data_instance

