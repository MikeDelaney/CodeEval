from multiples import multiples


def test_multiples_13_8():
    line = '13,8\n'
    assert multiples(line) == 16


def test_multiples_17_16():
    line = '17,16\n'
    assert multiples(line) == 32


def test_multiples_1710_64():
    line = '1710,64\n'
    assert multiples(line) == 1728
