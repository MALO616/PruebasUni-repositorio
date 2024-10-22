import pytest
from suma import suma

def test_num_positivo():

    assert suma(10, 8) == 18

def test_num_negativo():

    assert suma(-7, -3) == -10

def test_num_0():

    assert suma(0, 0) == 0
    
                