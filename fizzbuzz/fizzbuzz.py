import sys


def fb(a, b, n):
    a, b, n = int(a), int(b), int(n)
    if a == b:
        fb_dict = {a: 'FB'}
    else:
        fb_dict = {a: 'F', b: 'B'}
    retval = ''
    fb_out = ''
    for number in xrange(1, n + 1):
        for divisor in set((a, b)):
            if number % divisor == 0:
                fb_out += fb_dict.get(divisor)
        if fb_out:
            retval += fb_out + ' '
            fb_out = ''
        else:
            retval += str(number) + ' '
    return retval.rstrip()


if __name__ == '__main__':
    inputfile = sys.argv[1]
    with open(inputfile, 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            if line:
                a, b, n = tuple(line.split())
                print fb(a, b, n)
