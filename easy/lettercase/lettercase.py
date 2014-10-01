import sys


def lettercase(line):
    line = line.rstrip()
    lower_count = sum(map(str.islower, line))
    per_lower = lower_count * 100.0 / len(line)
    per_upper = 100.0 - per_lower
    return 'lowercase: {:.2f} uppercase: {:.2f}'.format(per_lower, per_upper)


if __name__ == '__main__':
    with open(sys.argv[1], 'rt') as f:
        for line in f:
            print lettercase(line)
