from mth_to_last import mth_to_last


def test_mth_to_last_input1():
    input_list = ['a', 'b', 'c', 'd', '4']
    expected = 'a'
    actual = mth_to_last(input_list)
    assert actual == expected


def test_mth_to_last_input2():
    input_list = ['e', 'f', 'g', 'h', '2']
    expected = 'g'
    actual = mth_to_last(input_list)
    assert actual == expected


def test_mth_to_last_out_of_range():
    input_list = ['a', 'b', 'c', 'd', '7']
    assert mth_to_last(input_list) is None
