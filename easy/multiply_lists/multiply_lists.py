import sys


def multiply_lists(list1, list2):
    retval = ''
    for i in xrange(len(list1)):
        retval += str(list1[i] * list2[i]) + ' '
    return retval.rstrip()


if __name__ == '__main__':
    inputfile = sys.argv[1]
    with open(inputfile, 'r') as f:
        for line in f:
            if line:
                line = line.split('|')
                print multiply_lists([int(item) for item in line[0].split()],
                                     [int(item) for item in line[1].split()])
