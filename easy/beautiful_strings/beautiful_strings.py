from collections import Counter
import string
import sys


def beautiful_strings(line):
    line = line.rstrip()
    if line:
        beauty = 0
        count = Counter(''.join(letter for letter in line.lower()
                                if letter in string.lowercase))
        for value in xrange(26, 26 - len(count), -1):
            if count:
                most_common = count.most_common(1)
                beauty += most_common[0][1] * value
                del count[most_common[0][0]]
        return beauty


if __name__ == '__main__':
    from pdb import set_trace; set_trace()
    with open(sys.argv[1], 'rt') as f:
        for line in f:
            print beautiful_strings(line)
