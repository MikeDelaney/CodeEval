import sys


def dec_to_bin(input_string):
    return bin(int(input_string))[2:]


if __name__ == '__main__':
    inputfile = sys.argv[1]
    with open(inputfile, 'r') as f:
        for line in f:
            if line:
                print dec_to_bin(line.strip())
