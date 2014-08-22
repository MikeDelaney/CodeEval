import sys


def lowest_unique(int_list):
    numbers = {i: [] for i in xrange(1, 10)}
    for index in range(len(int_list)):
        numbers[int(int_list[index])].append(index)
    for number in numbers:
        retval = numbers[number]
        if len(retval) == 1:
            return retval[0] + 1
    return 0


if __name__ == '__main__':
    inputfile = sys.argv[1]
    with open(inputfile, 'r') as f:
        for line in f:
            if line:
                print str(lowest_unique(line.rstrip().split()))
