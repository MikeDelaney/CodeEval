import sys


def non_repeated(a_string):
    for i in xrange(len(a_string)):
        if a_string[i] not in a_string[:i] + a_string[i+1:]:
            return a_string[i]


if __name__ == '__main__':
    inputfile = sys.argv[1]
    with open(inputfile, 'r') as f:
        for line in f:
            if line:
                print non_repeated(line.rstrip())
