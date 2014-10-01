from lettercase import lettercase


def test_lettercase_ex1():
    line = 'thisTHIS\n'
    assert lettercase(line) == 'lowercase: 50.00 uppercase: 50.00'


def test_lettercase_ex2():
    line = 'AAbbCCDDEE\n'
    assert lettercase(line) == 'lowercase: 20.00 uppercase: 80.00'


def test_lettercase_ex3():
    line = 'N\n'
    assert lettercase(line) == 'lowercase: 0.00 uppercase: 100.00'


def test_lettercase_ex4():
    line = 'UkJ\n'
    assert lettercase(line) == 'lowercase: 33.33 uppercase: 66.67'
