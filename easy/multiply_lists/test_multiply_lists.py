from multiply_lists import multiply_lists


def test_multiply_lists1():
    list1, list2 = [9, 0, 6], [15, 14, 9]
    expected = '135 0 54'
    actual = multiply_lists(list1, list2)
    assert actual == expected


def test_multiply_lists2():
    list1, list2 = [5], [8]
    expected = '40'
    actual = multiply_lists(list1, list2)
    assert actual == expected


def test_multiply_lists3():
    list1, list2 = [13, 4, 15, 1, 15, 5], [1, 4, 15, 14, 8, 2]
    expected = '13 16 225 14 120 10'
    actual = multiply_lists(list1, list2)
    assert actual == expected
