import sys


def array_absurdity(input_list):
    items = set()
    for item in input_list:
        if item in items:
            return item
        else:
            items |= {item}


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            newline = line.rstrip().split(';')[1].split(',')
            if newline:
                print array_absurdity(newline)
