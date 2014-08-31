from beautiful_strings import beautiful_strings


def test_beautiful_strings_ex1():
    input_string = 'ABbCcc\n'
    expected = 152
    actual = beautiful_strings(input_string)
    assert actual == expected


def test_beautiful_strings_ex2():
    input_string = 'Good luck in the Facebook Hacker Cup this year!\n'
    expected = 754
    actual = beautiful_strings(input_string)
    assert actual == expected


def test_beautiful_strings_ex3():
    input_string = 'Ignore punctuation, please :)\n'
    expected = 491
    actual = beautiful_strings(input_string)
    assert actual == expected


def test_beautiful_strings_ex4():
    input_string = 'Sometimes test cases are hard to make up.\n'
    expected = 729
    actual = beautiful_strings(input_string)
    assert actual == expected


def test_beautiful_strings_ex5():
    input_string = 'So I just go consult Professor Dalves\n'
    expected = 646
    actual = beautiful_strings(input_string)
    assert actual == expected
