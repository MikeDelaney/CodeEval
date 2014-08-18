from reverse import reverse_words


def test_reverse_words1():
    words = ['Hello', 'World']
    expected = 'World Hello'
    actual = reverse_words(words)
    assert actual == expected


def test_reverse_words2():
    words = ['Hello', 'CodeEval']
    expected = 'CodeEval Hello'
    actual = reverse_words(words)
    assert actual == expected
