import sys


def convert_zero(zero_list):
    pairs = [[zero_list[i], zero_list[i+1]]
             for i in xrange(0, len(zero_list), 2)]
    binstr = ''
    for item in pairs:
        if item[0] == '0':
            binstr += item[1]
        else:
            for digit in item[1]:
                binstr += '1'
    return int(binstr, 2)


# And now recursively, just for the fun of it
def convert_zero_rec(zero_list):
    binstr = _make_str(zero_list)
    return int(binstr, 2)


def _make_str(zero_list):
    if zero_list == []:
        return ''
    else:
        if zero_list[0] == '0':
            return zero_list[1] + _make_str(zero_list[2:])
        else:
            return zero_list[1].replace('0', '1') + _make_str(zero_list[2:])

if __name__ == '__main__':
    inputfile = sys.argv[1]
    with open(inputfile, 'r') as f:
        for line in f.readlines():
            line = line.rstrip().split()
            if line:
                print convert_zero(line)
