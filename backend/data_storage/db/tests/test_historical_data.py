# data_storage/db/tests/test_historical_data.py
import pytest
from api.models import HistoricalData

def test_insert_historical_data(db, historical_data):
    assert HistoricalData.objects.count() == 1

def test_update_historical_data(db, historical_data):
    historical_data.price = 42
    historical_data.save()
    updated_historical_data = HistoricalData.objects.get(id=historical_data.id)
    assert updated_historical_data.price == 42

def test_retrieve_historical_data(db, historical_data):
    retrieved_historical_data = HistoricalData.objects.get(id=historical_data.id)
    assert retrieved_historical_data == historical_data
