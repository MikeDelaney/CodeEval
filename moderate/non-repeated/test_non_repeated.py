from non_repeated import non_repeated


def test_non_repeated_yellow():
    assert non_repeated('yellow') == 'y'


def test_non_repeated_first():
    assert non_repeated('first') == 'f'


def test_non_repeated_seconds():
    assert non_repeated('seconds') == 'e'


def test_non_repeated_tooth():
    assert non_repeated('tooth') == 'h'
