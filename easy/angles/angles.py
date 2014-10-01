import math
import sys


def splitnum(num):
    frac, whole = math.modf(num)
    return frac, int(whole)


def angles(line):
    line = float(line.rstrip())
    minutes, main = splitnum(line)
    seconds, minutes = splitnum(minutes * 60)
    seconds = int(seconds * 60)
    return '{}.{:02d}\'{:02d}"'.format(main, minutes, seconds)


if __name__ == '__main__':
    with open(sys.argv[1], 'rt') as f:
        for line in f:
            print angles(line)
