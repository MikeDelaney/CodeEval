from num_ones import num_ones


def test_num_ones_10():
    assert num_ones('10\n') == 2


def test_num_ones_22():
    assert num_ones('22\n') == 3


def test_num_ones_56():
    assert num_ones('56') == 3


def test_num_ones_empty():
    assert num_ones('\n') is None
