import sys


if __name__ == '__main__':
    endianness = {'little': 'LittleEndian', 'big': 'BigEndian'}
    print endianness[sys.byteorder]
