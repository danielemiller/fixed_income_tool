# data_storage/db/tests/test_valuation_metrics.py
import pytest
from backend.api.models import ValuationMetrics

def test_insert_valuation_metrics(db, valuation_metrics):
    assert ValuationMetrics.objects.count() == 1

def test_update_valuation_metrics(db, valuation_metrics):
    valuation_metrics.metric_a = 200
    valuation_metrics.save()
    updated_valuation_metrics = ValuationMetrics.objects.get(id=valuation_metrics.id)
    assert updated_valuation_metrics.metric_a == 200

def test_retrieve_valuation_metrics(db, valuation_metrics):
    retrieved_valuation_metrics = ValuationMetrics.objects.get(id=valuation_metrics.id)
    assert retrieved_valuation_metrics == valuation_metrics
