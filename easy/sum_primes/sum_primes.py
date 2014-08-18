
def gen_primes():
    # logic from Sieve of Eratosthenes
    # by David Eppstein, UC Irvine, 28 Feb 2002
    # http://code.activestate.com/recipes/117119/
    # changed var names
    sieve = {}
    check_int = 2
    while True:
        if check_int not in sieve:
            yield check_int
            sieve[check_int * check_int] = [check_int]
        else:
            for number in sieve[check_int]:
                sieve.setdefault(number + check_int, []).append(number)
            del sieve[check_int]
        check_int += 1


if __name__ == '__main__':
    sum = 0
    primes = gen_primes()
    for i in xrange(1000):
        sum += primes.next()
    print sum
