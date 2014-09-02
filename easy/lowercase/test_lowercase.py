from lowercase import lowercase


def test_lowercase_ex1():
    input_string = 'HELLO CODEEVAL\n'
    expected = 'hello codeeval'
    actual = lowercase(input_string)
    assert actual == expected


def test_lowercase_ex2():
    input_string = 'This is some text\n'
    expected = 'this is some text'
    actual = lowercase(input_string)
    assert actual == expected
