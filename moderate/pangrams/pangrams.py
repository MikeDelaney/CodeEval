import string
import sys


def pangrams(line, alpha):
    line = line.rstrip()
    if line:
        chars = set(line.lower())
        remaining = alpha.difference(chars)
        if remaining:
            return ''.join(list(sorted(remaining)))
        return 'NULL'


if __name__ == '__main__':
    with open(sys.argv[1], 'rt') as f:
        alpha = set(string.lowercase)
        for line in f:
            print pangrams(line, alpha)
