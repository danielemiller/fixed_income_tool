# data_storage/db/tests/test_risk_analysis_metrics.py
import pytest
from api.models import RiskAnalysisMetrics
from decimal import Decimal

def test_insert_risk_analysis_metrics(db, risk_analysis_metrics):
    assert RiskAnalysisMetrics.objects.count() == 1

def test_update_risk_analysis_metrics(db, risk_analysis_metrics):
    risk_analysis_metrics.yield_to_call = 3.14
    risk_analysis_metrics.average_life = 10.1
    risk_analysis_metrics.option_adjusted_spread = 4.2
    risk_analysis_metrics.risk_free_yield = 1.2
    risk_analysis_metrics.save()
    updated_risk_analysis_metrics = RiskAnalysisMetrics.objects.get(id=risk_analysis_metrics.id)
    assert updated_risk_analysis_metrics.yield_to_call == Decimal('3.14')
    assert updated_risk_analysis_metrics.average_life == Decimal('10.1')
    assert updated_risk_analysis_metrics.option_adjusted_spread == Decimal('4.2')
    assert updated_risk_analysis_metrics.risk_free_yield == Decimal('1.2')

def test_retrieve_risk_analysis_metrics(db, risk_analysis_metrics):
    retrieved_risk_analysis_metrics = RiskAnalysisMetrics.objects.get(id=risk_analysis_metrics.id)
    assert retrieved_risk_analysis_metrics == risk_analysis_metrics
