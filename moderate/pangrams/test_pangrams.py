import string
from pangrams import pangrams
import pytest


@pytest.fixture(scope='session')
def alpha():
    return set(string.lowercase)


def test_pangrams_true(alpha):
    alpha = alpha
    input_string = 'A quick brown fox jumps over the lazy dog'
    expected = 'NULL'
    actual = pangrams(input_string, alpha)
    assert actual == expected


def test_pangrams_false(alpha):
    alpha = alpha
    input_string = 'A slow yellow fox crawls under the proactive dog'
    expected = 'bjkmqz'
    actual = pangrams(input_string, alpha)
    assert actual == expected
