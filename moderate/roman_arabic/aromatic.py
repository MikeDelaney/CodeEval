import sys
import operator


def aromatic(target_string, roman):
    pairs = [[int(target_string[i]), roman[target_string[i+1]]]
             for i in xrange(0, len(target_string) - 1, 2)]
    for i in xrange(len(pairs) - 1):
        if pairs[i][1] < pairs[i+1][1]:
            pairs[i][1] *= -1
    return sum([reduce(operator.mul, item) for item in pairs])


if __name__ == '__main__':
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
             'D': 500, 'M': 1000}
    inputfile = sys.argv[1]
    with open(inputfile, 'r') as f:
        for line in f:
            if line:
                print aromatic(line.rstrip(), roman)
