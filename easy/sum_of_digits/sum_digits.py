import sys


def sum_digits(line):
    line = line.rstrip()
    sum = 0
    if line:
        for item in line:
            sum += int(item)
        return sum


if __name__ == '__main__':
    with open(sys.argv[1], 'rt') as f:
        for line in f:
            print sum_digits(line)
