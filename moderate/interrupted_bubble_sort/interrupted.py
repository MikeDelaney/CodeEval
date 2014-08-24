import sys


def interrupted(number_list, iterations):
    iter_count = 0
    is_sorted = False
    while iter_count < iterations and is_sorted is False:
        is_sorted = True
        for i in xrange(len(number_list) - 1):
            if number_list[i] > number_list[i+1]:
                number_list[i], number_list[i+1] = number_list[i+1], \
                    number_list[i]
                is_sorted = False
        iter_count += 1
    return ' '.join([str(item) for item in number_list])


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            newline = line.rstrip().split('|')
            iterations = int(newline[1])
            num_list = [int(item) for item in newline[0].split()]
            print interrupted(num_list, iterations)
