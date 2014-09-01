from over_rect import over_rect


def test_over_rect_ex1():
    input_string = '-3,3,-1,1,1,-1,3,-3\n'
    assert over_rect(input_string) is False


def test_over_rect_ex2():
    input_string = '-3,3,-1,1,-2,4,2,2\n'
    assert over_rect(input_string) is True


def test_over_rect_blank():
    input_string = '\n'
    assert over_rect(input_string) is None
