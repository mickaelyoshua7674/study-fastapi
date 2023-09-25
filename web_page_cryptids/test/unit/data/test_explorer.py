import os
import pytest
from model.explorer import Explorer
from errors.errors import Missing, Duplicate

# Set this before data.init to make SQLite work completely in memory
os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
from ....data import explorer

@pytest.fixture
def sample() -> Explorer:
    return Explorer(name="Bob",
                    nationality="Brazil")

def test_create(sample):
    resp = explorer.create(sample)
    assert resp == sample

def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        resp = explorer.create(sample)

def test_get(sample):
    resp = explorer.get_one(sample.name)
    assert resp == sample

def test_get_missing():
    with pytest.raises(Missing):
        resp = explorer.get_one("boxturtle")

def test_modify(sample):
    sample.location = "Sesame Street"
    resp = explorer.modify(sample.name, sample)
    assert resp == sample

def test_modigy_missing():
    bob: Explorer = Explorer(name="Bill",
                             nationality="India")
    with pytest.raises(Missing):
        resp = explorer.modify(bob.name, bob)

def test_delete(sample):
    resp = explorer.delete(sample.name)
    assert resp is None

def test_delete_missing(sample):
    with pytest.raises(Missing):
        resp = explorer.delete(sample.name)