from primes import primes


def test_primes_10():
    assert primes(10) == '2,3,5,7'


def test_primes_20():
    assert primes(20) == '2,3,5,7,11,13,17,19'


def test_primes_100():
    assert primes(100) == '2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,'\
        '53,59,61,67,71,73,79,83,89,97'
