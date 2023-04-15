# data_storage/db/tests/test_bond.py
import pytest
from api.models import BondData

def test_insert_bond(db, bond):
    assert BondData.objects.count() == 1

def test_update_bond(db, bond):
    bond.issuer = "New Test Issuer"
    bond.save()
    updated_bond = BondData.objects.get(id=bond.id)
    assert updated_bond.issuer == "New Test Issuer"

def test_retrieve_bond(db, bond):
    retrieved_bond = BondData.objects.get(id=bond.id)
    assert retrieved_bond == bond
