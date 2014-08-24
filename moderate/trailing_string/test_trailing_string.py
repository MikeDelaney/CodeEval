from trailing_string import trailing_string


def test_trailing_string_ex1():
    input_list = ['Hello World', 'World']
    assert trailing_string(input_list) == 1


def test_trailing_string_ex2():
    input_list = ['Hello CodeEval', 'CodeEval']
    assert trailing_string(input_list) == 1


def test_trailing_string_ex3():
    input_list = ['San Francisco', 'San Jose']
    assert trailing_string(input_list) == 0
