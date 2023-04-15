# data_storage/db/tests/test_bond.py
import pytest
from backend.api.models import Bond

def test_insert_bond(db, bond):
    assert Bond.objects.count() == 1

def test_update_bond(db, bond):
    bond.issuer = "New Test Issuer"
    bond.save()
    updated_bond = Bond.objects.get(id=bond.id)
    assert updated_bond.issuer == "New Test Issuer"

def test_retrieve_bond(db, bond):
    retrieved_bond = Bond.objects.get(id=bond.id)
    assert retrieved_bond == bond
