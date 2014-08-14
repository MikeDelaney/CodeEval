import sys


def longest(lines):
    retnum = int(lines.pop(0)) * -1
    lines.sort(key=len)
    lines = lines[retnum:][::-1]
    return ''.join(lines)


if __name__ == '__main__':
    inputfile = sys.argv[1]
    with open(inputfile, 'r') as f:
        lines = f.readlines()
    print longest(lines)
