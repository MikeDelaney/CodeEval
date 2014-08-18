import sys


def reverse_words(words):
    return ' '.join(words[::-1])


if __name__ == '__main__':
    inputfile = sys.argv[1]
    with open(inputfile, 'r') as f:
        for line in f.readlines():
            line = line.rstrip().split()
            if line:
                print reverse_words(line)
