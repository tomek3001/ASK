import textwrap
import re

char_size = 10


def string2binary(string, separate_letters=True):
    connector = ' '
    if not separate_letters:
        connector = ''
    binary_string = connector.join(format(ord(letter), 'b').rjust(char_size, '0') for letter in string)
    binary_string = binary_string[::-1]
    coded_binary_string = code_rs232(binary_string)
    return coded_binary_string


def binary2string(string):
    decoded_binary = decode_rs232(string)[::-1]
    separated_letters = textwrap.wrap(decoded_binary, char_size)
    ascii_string = ''.join(chr(int(letter, 2)) for letter in separated_letters)
    return ascii_string


def code_rs232(string):
    frame = '011'
    separated_letters = textwrap.wrap(string, char_size)
    coded_string = ''.join(frame[:1] + letter + frame[1:] for letter in separated_letters)
    return coded_string


def decode_rs232(string):
    separated_letters = textwrap.wrap(string, char_size + 3)
    decoded_string = ''.join(letter[1:-2] for letter in separated_letters)
    return decoded_string


def censore_message(message, ldict):
    message_temp = message.split(" ")
    for word in ldict:
        censor = re.compile(word, re.ASCII)
        message = censor.sub(''.rjust(len(word), '*'), message.lower())
    result_message = ""
    message = message.split(" ")
    for word in range(len(message_temp)):
        if "*" in message[word]:
            result_message += message[word]
        else:
            result_message += message_temp[word]
        result_message += " "

    return result_message





