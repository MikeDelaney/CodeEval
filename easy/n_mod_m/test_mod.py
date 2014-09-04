from mod import mod


def test_mod_20_6():
    line = '20,6\n'
    expected = 20 % 6
    actual = mod(line)
    assert actual == expected


def test_mod_2_3():
    line = '2,3\n'
    expected = 2 % 3
    actual = mod(line)
    assert actual == expected
