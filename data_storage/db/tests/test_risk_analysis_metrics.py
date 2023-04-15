# data_storage/db/tests/test_risk_analysis_metrics.py
import pytest
from backend.api.models import RiskAnalysisMetrics

def test_insert_risk_analysis_metrics(db, risk_analysis_metrics):
    assert RiskAnalysisMetrics.objects.count() == 1

def test_update_risk_analysis_metrics(db, risk_analysis_metrics):
    risk_analysis_metrics.metric_x = "New Value"
    risk_analysis_metrics.save()
    updated_risk_analysis_metrics = RiskAnalysisMetrics.objects.get(id=risk_analysis_metrics.id)
    assert updated_risk_analysis_metrics.metric_x == "New Value"

def test_retrieve_risk_analysis_metrics(db, risk_analysis_metrics):
    retrieved_risk_analysis_metrics = RiskAnalysisMetrics.objects.get(id=risk_analysis_metrics.id)
    assert retrieved_risk_analysis_metrics == risk_analysis_metrics
