from reverse_add import reverse_add, reverse_number


def test_reverse_number():
    assert reverse_number(84) == 48


def test_reverse_add_ex_1():
    assert reverse_add(195) == '4 9339'


def test_reverse_add_43():
    assert reverse_add(43) == '1 77'
