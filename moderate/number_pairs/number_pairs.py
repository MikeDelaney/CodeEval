import sys


def number_pairs(input_list, x):
    retval = 'NULL'
    checked = set([])
    for number in input_list:
        if number < x:
            diff = x - number
            if diff in input_list and diff not in checked:
                checked = checked | {number}
                retval += '{0},{1};'.format(number, diff)
    if len(retval) > 4:
        return retval[4:-1]
    return retval


if __name__ == '__main__':
    inputfile = sys.argv[1]
    with open(inputfile, 'r') as f:
        for line in f.readlines():
            line = line.rstrip().split(';')
            if line:
                input_list, x = [int(num) for num in line[0].split(',')],\
                    int(line[1])
                print number_pairs(input_list, x)
