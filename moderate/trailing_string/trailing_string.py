import sys
import csv


def trailing_string(line_list):
    target_string = line_list[1]
    search_string = line_list[0]
    if search_string[len(target_string) * -1:] == target_string:
        return 1
    return 0


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in csv.reader(f):
            if line:
                print trailing_string(line)
