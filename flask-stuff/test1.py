import pytest
from sample_backend import *

def test_new_id():
    assert isinstance(make_id(), str)

#gotta write test cases for code coverage
