import sys


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


def primes(limit):
    retval = ''
    prime = gen_primes()
    number = prime.next()
    while number < limit:
        retval += str(number) + ','
        number = prime.next()
    return retval[:-1]


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            line = int(line.rstrip())
            if line:
                print primes(line)
