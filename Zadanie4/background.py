
def sting2binary(string, separate_letters=True):

    connecotr = ' '
    if not separate_letters:
        connector = ''
    binary_string = connector.join(format(ord(letter), 'b') for letter in string)
    return binary_string

