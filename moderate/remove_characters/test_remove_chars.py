from remove_chars import remove_chars


def test_remove_chars1():
    in_string, letters = 'how are you', 'abc'
    expected = 'how re you'
    actual = remove_chars(in_string, letters)
    assert actual == expected


def test_remove_chars2():
    in_string, letters = 'hello world', 'def'
    expected = 'hllo worl'
    actual = remove_chars(in_string, letters)
    assert actual == expected
