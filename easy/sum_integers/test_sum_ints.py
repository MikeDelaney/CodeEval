from sum_ints import sum_ints


def test_sum_ints_ex1():
    inputs = ['5\n', '12\n']
    assert sum_ints(inputs) == 17


def test_sum_ints_ex2():
    inputs = ['12\n', '\n', '14\n']
    assert sum_ints(inputs) == 26
