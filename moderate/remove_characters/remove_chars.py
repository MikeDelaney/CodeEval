import sys


def remove_chars(a_string, letters):
    for letter in letters:
        a_string = a_string.replace(letter, '')
    return a_string


if __name__ == '__main__':
    inputfile = sys.argv[1]
    with open(inputfile, 'r') as f:
        for line in f:
            if line:
                target_string, letters = line.rstrip().split(', ')
                print remove_chars(target_string, letters)
