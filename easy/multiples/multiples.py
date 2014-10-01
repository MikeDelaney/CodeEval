import sys


def multiples(line):
    x, n = (int(item) for item in line.rstrip().split(','))
    retval = n
    while retval < x:
        retval += n
    return retval


if __name__ == '__main__':
    with open(sys.argv[1], 'rt') as f:
        for line in f:
            print multiples(line)
