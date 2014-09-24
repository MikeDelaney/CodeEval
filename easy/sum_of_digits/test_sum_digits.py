from sum_digits import sum_digits


def test_sum_digits_23():
    line = '23\n'
    assert sum_digits(line) == 5


def test_sum_digits_496():
    line = '496\n'
    assert sum_digits(line) == 19
