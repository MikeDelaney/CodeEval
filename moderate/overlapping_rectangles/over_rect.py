import sys


def over_rect(line):
    line = line.rstrip()
    if line:
        line = line.split(',')
        rect_a = [int(item) for item in line[:4]]
        rect_b = [int(item) for item in line[4:]]
        return (rect_a[0] <= rect_b[0] <= rect_a[2] and
                (rect_a[3] <= rect_b[1] <= rect_a[1] or
                rect_a[3] <= rect_b[3] <= rect_a[1])) or \
            (rect_b[0] <= rect_a[0] <= rect_b[2] and
                (rect_b[3] <= rect_a[1] <= rect_b[1] or
                    rect_b[3] <= rect_a[3] <= rect_b[1]))


if __name__ == '__main__':
    with open(sys.argv[1], 'rt') as f:
        for line in f:
            print over_rect(line)
