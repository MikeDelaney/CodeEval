from prime_palindrome import is_palindrome


def test_is_palindrome_returns_false():
    number = 24
    assert is_palindrome(number) is False


def test_is_palindrome_returns_true():
    number = 8448
    assert is_palindrome(number) is True
