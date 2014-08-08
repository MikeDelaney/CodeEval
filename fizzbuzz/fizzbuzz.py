import sys


def fb(a, b, n):
    a, b, n = int(a), int(b), int(n)
    retval = ''
    for number in xrange(1, n + 1):
        a_remainder = number % a
        b_remainder = number % b
        if not a_remainder and not b_remainder:
            retval += 'FB '
        elif not a_remainder:
            retval += 'F '
        elif not b_remainder:
            retval += 'B '
        else:
            retval += str(number) + ' '
    return retval.rstrip()

if __name__ == '__main__':
    inputfile = sys.argv[1]
    with open(inputfile, 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            if line:
                a, b, n = tuple(line.split())
                print fb(a, b, n)
