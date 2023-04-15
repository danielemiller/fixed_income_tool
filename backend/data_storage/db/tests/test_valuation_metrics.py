# data_storage/db/tests/test_valuation_metrics.py
import pytest
from decimal import Decimal
from api.models import ValuationMetrics

def test_insert_valuation_metrics(db, valuation_metrics):
    assert ValuationMetrics.objects.count() == 1

def test_update_valuation_metrics(db, valuation_metrics):
    valuation_metrics.bond_price = 100.50
    valuation_metrics.yield_to_maturity = 2.75
    valuation_metrics.modified_duration = 4.5
    valuation_metrics.macaulay_duration = 3.8
    valuation_metrics.convexity = 0.20
    valuation_metrics.credit_spread = 1.20
    valuation_metrics.save()
    updated_valuation_metrics = ValuationMetrics.objects.get(id=valuation_metrics.id)
    assert updated_valuation_metrics.bond_price == Decimal('100.50')
    assert updated_valuation_metrics.yield_to_maturity == Decimal('2.75')
    assert updated_valuation_metrics.modified_duration == Decimal('4.5')
    assert updated_valuation_metrics.macaulay_duration == Decimal('3.8')
    assert updated_valuation_metrics.convexity == Decimal('0.20')
    assert updated_valuation_metrics.credit_spread == Decimal('1.20')

def test_retrieve_valuation_metrics(db, valuation_metrics):
    retrieved_valuation_metrics = ValuationMetrics.objects.get(id=valuation_metrics.id)
    assert retrieved_valuation_metrics == valuation_metrics
