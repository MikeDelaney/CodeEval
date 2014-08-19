import pytest
from aromatic import aromatic


@pytest.fixture(scope="session")
def trans_dict():
    trans_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                  'D': 500, 'M': 1000}
    return trans_dict

def test_aromatic1(trans_dict):
    translation = trans_dict
    target = '3M1D2C'
    expected = 3700
    actual = aromatic(target, translation)
    assert actual == expected


def test_aromatic2(trans_dict):
    translation = trans_dict
    target = '2I3I2X9V1X'
    expected = -16
    actual = aromatic(target, translation)
    assert actual == expected
