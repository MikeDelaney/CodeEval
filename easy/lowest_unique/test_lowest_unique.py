from lowest_unique import lowest_unique


def test_lowest_unique_ex1():
    input_list = [3, 3, 9, 1, 6, 5, 8, 1, 5, 3]
    assert lowest_unique(input_list) == 5


def test_lowest_unique_ex2():
    input_list = [9, 2, 9, 9, 1, 8, 8, 8, 2, 1, 1]
    assert lowest_unique(input_list) == 0
