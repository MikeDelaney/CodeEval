import sys


def mod(line):
    number, divisor = (int(i) for i in line.rstrip().split(','))
    if number < divisor:
        return number
    return number - int(float(number) / divisor) * divisor


if __name__ == '__main__':
    with open(sys.argv[1], 'rt') as f:
        for line in f:
            print mod(line)
