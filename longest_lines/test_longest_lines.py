from longest_lines import longest


def test_longest():
    lines = ['2',
             'Hello World\n',
             'CodeEval\n',
             'Quick Fox\n',
             'A\n',
             'San Francisco\n']
    expected = 'San Francisco\nHello World\n'
    actual = longest(lines)
    assert actual == expected
