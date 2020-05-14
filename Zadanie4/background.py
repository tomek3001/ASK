import textwrap


def string2binary(string, separate_letters=True):
    connector = ' '
    if not separate_letters:
        connector = ''
    binary_string = connector.join(format(ord(letter), 'b') for letter in string)
    coded_binary_string = code_rs232(binary_string)
    return coded_binary_string


def binary2string(string):
    decoded_binary = decode_rs232(string)
    separated_letters = textwrap.wrap(decoded_binary, 7)
    ascii_string = ''.join(chr(int(letter, 2)) for letter in separated_letters)
    return ascii_string


def code_rs232(string):
    frame = '011'
    separated_letters = textwrap.wrap(string, 7)
    coded_string = ''.join(frame[:1] + letter + frame[1:] for letter in separated_letters)
    return coded_string


def decode_rs232(string):
    separated_letters = textwrap.wrap(string, 10)
    decoded_string = ''.join(letter[1:-2] for letter in separated_letters)
    return decoded_string
