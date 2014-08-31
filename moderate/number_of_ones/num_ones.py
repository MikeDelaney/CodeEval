import sys


def num_ones(line):
    line = line.rstrip()
    if line:
        return bin(int(line)).count('1')


if __name__ == '__main__':
    with open(sys.argv[1], 'rt') as f:
        for line in f:
            print num_ones(line)
