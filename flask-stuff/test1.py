import pytest
from sample_backend import make_id

def test_new_id():
    assert isinstance(make_id(), str)
