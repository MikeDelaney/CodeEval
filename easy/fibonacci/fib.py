import sys


def fib(number):
    if not number:
        return 0
    if number == 1:
        return 1
    return fib(number - 1) + fib(number - 2)


if __name__ == '__main__':
    inputfile = sys.argv[1]
    with open(inputfile, 'r') as f:
        for line in f:
            if line:
                print '{}'.format(fib(int(line.strip())))
