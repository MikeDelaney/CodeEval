import sys


def lowercase(line):
    line = line.rstrip()
    if line:
        return line.lower()


if __name__ == '__main__':
    with open(sys.argv[1], 'rt') as f:
        for line in f:
            print lowercase(line)
