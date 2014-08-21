
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


def is_palindrome(number):
    return str(number) == ''.join(reversed(str(number)))


if __name__ == '__main__':
    largest = 0
    primes = gen_primes()
    prime = primes.next()
    while prime < 1000:
        if is_palindrome(prime):
            largest = prime
        prime = primes.next()
    print largest
