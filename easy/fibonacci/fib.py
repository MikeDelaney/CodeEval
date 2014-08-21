import sys


def genfib():
    first, second = 0, 1
    while True:
        yield first
        first, second = second, first + second


def fib(number):
    fibs = genfib()
    for i in xrange(number + 1):
        retval = fibs.next()
    return retval


if __name__ == '__main__':
    inputfile = sys.argv[1]
    with open(inputfile, 'r') as f:
        for line in f:
            if line:
                print '{}'.format(fib(int(line.strip())))
