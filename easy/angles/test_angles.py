from angles import angles


def test_angles_ex1():
    line = '330.39991833\n'
    assert angles(line) == '330.23\'59\"'


def test_angles_ex2():
    line = '0.001\n'
    assert angles(line) == '0.00\'03\"'


def test_angles_ex3():
    line = '14.64530319\n'
    assert angles(line) == '14.38\'43\"'


def test_angles_ex4():
    line = '0.25\n'
    assert angles(line) == '0.15\'00\"'


def test_angles_ex5():
    line = '254.16991217\n'
    assert angles(line) == '254.10\'11\"'
