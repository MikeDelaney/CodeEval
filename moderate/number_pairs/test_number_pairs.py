from number_pairs import number_pairs


def test_number_pairs1():
    input_list, x = [1, 2, 3, 4, 6], 5
    expected = '1,4;2,3'
    actual = number_pairs(input_list, x)
    assert actual == expected


def test_number_pairs2():
    input_list, x = [2, 4, 5, 6, 9, 11, 15], 20
    expected = '5,15;9,11'
    actual = number_pairs(input_list, x)
    assert actual == expected


def test_number_pairs3():
    input_list, x = [1, 2, 3, 4], 50
    expected = 'NULL'
    actual = number_pairs(input_list, x)
    assert actual == expected
