"""
'Toolbox', A small library of tools for personal use.
Functional tools: to_hex(), to_binary()
"""


# Functions
def to_hex(input, type):
    """
    This function can translate both unicode and binary into hexadecimal.
    :param input: The input, that which you intend to translate.
    :param type: STR for strings (unicode), HEX for hexadecimal.
    :return:
    """
    if type == 'STR':
        hex_message = input.encode('utf-8').hex()
    elif type == 'BIN':
        hex_message = hex(int(input, 2))[2:]
    hex_list = [hex_message[index: index + 2] for index in range(0, len(hex_message), 2)]
    return ' '.join(hex_list)


def to_binary(input, type):
    """
    This function can translate both unicode and hexadecimal into (8-bits) binary.
    :param input: The input, that which you intend to translate.
    :param type: STR for strings (unicode), HEX for hexadecimal.
    :return:
    """
    if type == 'STR':
        return ' '.join(format(i, '08b') for i in bytearray(input, encoding='utf-8'))
    elif type == 'HEX':
        in_bin = bin(int('1' + input.replace(" ", ""), 16))[3:]
        return ' '.join([in_bin[index: index + 8] for index in range(0, len(in_bin), 8)])


# Main, only used to test functions.
if __name__ == '__main__':
    message = 'This is a test string!'
    print()
    print('FUNCTION TEST: to_hex(string)')
    print(f'original STR: {message}\n'
          f'from STR to HEX: {to_hex(message, "STR")}\n'
          f'from BIN to HEX: {to_hex(to_binary(message, "STR").replace(" ", ""), "BIN")}')

    print()
    print('FUNCTION TEST: to_binary(input, type)')
    print(f'original STR: {message}\n'
          f'from STR to Binary: {to_binary(message, "STR")}\n'
          f'from HEX to Binary: {to_binary(to_hex(message, "STR").replace(" ", ""), "HEX")}')
