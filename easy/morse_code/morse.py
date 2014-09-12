import sys

morse_dict = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '-----': '0',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    }


def morse(line):
    line = line.rstrip()
    if line:
        words = line.split('  ')
        for i in xrange(len(words)):
            words[i] = translate(words[i])
        return ' '.join(words)


def translate(word):
    retval = ''
    letters = word.split()
    for letter in letters:
        retval += morse_dict[letter]
    return retval


if __name__ == '__main__':
    with open(sys.argv[1], 'rt') as f:
        for line in f:
            print morse(line)
