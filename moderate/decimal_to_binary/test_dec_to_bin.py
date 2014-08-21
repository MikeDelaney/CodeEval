from dec_to_bin import dec_to_bin


def test_dec_to_bin_2():
    input_val = '2'
    expected = '10'
    actual = dec_to_bin(input_val)
    assert actual == expected


def test_dec_to_bin_10():
    input_val = '10'
    expected = '1010'
    actual = dec_to_bin(input_val)
    assert actual == expected


def test_dec_to_bin_67():
    input_val = '67'
    expected = '1000011'
    actual = dec_to_bin(input_val)
    assert actual == expected
