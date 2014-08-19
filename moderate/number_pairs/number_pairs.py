import sys
from itertools import combinations


def number_pairs(input_list, x):
    """
    Inspired by https://gist.github.com/yuhei0718/2765371
    My solution was much clunkier
    """
    pairs = [combo for combo in combinations(input_list, 2) if sum(combo) == x]
    if pairs:
        return ';'.join(['{0},{1}'.format(item[0], item[1])for item in pairs])
    return 'NULL'


if __name__ == '__main__':
    inputfile = sys.argv[1]
    with open(inputfile, 'r') as f:
        for line in f.readlines():
            line = line.rstrip().split(';')
            if line:
                input_list, x = [int(num) for num in line[0].split(',')],\
                    int(line[1])
                print number_pairs(input_list, x)
