from morse import morse


def test_morse_4():
    assert morse('....-\n') == '4'


def test_morse_ex1():
    line = '.- ...- ..--- .-- .... .. . -.-. -..-  ....- .....\n'
    assert morse(line) == 'AV2WHIECX 45'


def test_morse_ex2():
    line = '-... .... ...--\n'
    assert morse(line) == 'BH3'
