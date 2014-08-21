import sys


def mth_to_last(char_list):
    index = int(char_list.pop())
    if index <= len(char_list):
        return char_list[index * -1]


if __name__ == '__main__':
    inputfile = sys.argv[1]
    with open(inputfile, 'r') as f:
        for line in f:
            line = line.rstrip().split()
            result = mth_to_last(line)
            if result:
                print result
