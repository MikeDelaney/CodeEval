import sys


def over_rect(line):
    line = line.rstrip()
    if line:
        xula, yula, xlra, ylra, xulb, yulb, xlrb, ylrb = (int(i) for i
                                                          in line.split(','))
        h_overlap = True
        v_overlap = True
        if xlrb < xula or xulb > xlra:
            h_overlap = False
        if yulb < ylra or ylrb > yula:
            v_overlap = False
        return h_overlap and v_overlap


if __name__ == '__main__':
    with open(sys.argv[1], 'rt') as f:
        for line in f:
            print over_rect(line)
