import sys


def lowest_unique(int_list):
    numbers = {}
    for index, number in enumerate(int_list):
        group = numbers.setdefault(int(number), [])
        group.append(index)
    for number in sorted(numbers.keys()):
        retval = numbers[number]
        if len(retval) == 1:
            return retval[0] + 1
    return 0


if __name__ == '__main__':
    inputfile = sys.argv[1]
    with open(inputfile, 'r') as f:
        for line in f:
            line_list = line.rstrip().split()
            if line_list:
                print str(lowest_unique(line_list))
