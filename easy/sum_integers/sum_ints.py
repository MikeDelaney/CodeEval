import sys


def sum_ints(iterable):
    return sum([int(item.rstrip()) for item in iterable if item.rstrip()])


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        print sum_ints(f)
