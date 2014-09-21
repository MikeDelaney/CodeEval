import sys
import string


def rollercoaster(line, rejects):
    line = line.rstrip()
    index = 0
    retval = ''
    for char in line:
        if char not in rejects:
            if index % 2 == 0:
                char = char.upper()
            else:
                char = char.lower()
            index += 1
        retval += char
    return retval


if __name__ == '__main__':
    with open(sys.argv[1], 'rt') as f:
        rejects = string.punctuation + ' '
        for line in f:
            print rollercoaster(line, rejects)
