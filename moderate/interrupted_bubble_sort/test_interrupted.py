from interrupted import interrupted


def test_interrupted_ex1():
    input_list = [36, 47, 78, 28, 20, 79, 87, 16, 8, 45, 72, 69, 81, 66, 60, 8,
                  3, 86, 90, 90]
    iterations = 1
    expected = '36 47 28 20 78 79 16 8 45 72 69 81 66 60 8 3 86 87 90 90'
    actual = interrupted(input_list, iterations)
    assert actual == expected


def test_interrupted_ex2():
    input_list = [40, 69, 52, 42, 24, 16, 66]
    iterations = 2
    expected = '40 42 24 16 52 66 69'
    actual = interrupted(input_list, iterations)
    assert actual == expected


def test_interrupted_ex3():
    input_list = [54, 46, 0, 34, 15, 48, 47, 53, 25, 18, 50, 5, 21, 76, 62, 48,
                  74, 1, 43, 74, 78, 29]
    iterations = 6
    expected = '0 15 25 18 34 5 21 46 47 48 48 1 43 50 53 29 54 62 74 74 76 78'
    actual = interrupted(input_list, iterations)
    assert actual == expected


def test_interrupted_ex4():
    input_list = [48, 51, 5, 61, 18]
    iterations = 2
    expected = '5 48 18 51 61'
    actual = interrupted(input_list, iterations)
    assert actual == expected


def test_interrupted_ex5():
    input_list = [59, 68, 55, 31, 73, 4, 1, 25, 26, 19, 60, 0]
    iterations = 2
    expected = '55 31 59 4 1 25 26 19 60 0 68 73'
    actual = interrupted(input_list, iterations)
    assert actual == expected


def test_interrupted_empty():
    input_list = []
    iterations = 2
    expected = ''
    actual = interrupted(input_list, iterations)
    assert actual == expected


def test_interrupted_no_iterations():
    input_list = [48, 51, 5, 61, 18]
    iterations = 0
    expected = '48 51 5 61 18'
    actual = interrupted(input_list, iterations)
    assert actual == expected


def test_interrupted_1_item_list():
    input_list = [1]
    iterations = 2
    expected = '1'
    actual = interrupted(input_list, iterations)
    assert actual == expected
