import sys


def reverse_add(line):
    number = int(line.rstrip())
    count = 0
    while not is_palindrome(number) and count < 100:
        number += reverse_number(number)
        count += 1
    return '{0} {1}'.format(count, number)


def reverse_number(number):
    reversed_num = 0
    num = number
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num / 10
    return reversed_num


def is_palindrome(number):
    return number == reverse_number(number)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            print reverse_add(line)
