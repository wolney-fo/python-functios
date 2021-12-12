from random import randint


def get_hex():
    hexadecimal_digits = '0123456789abcdef'
    hex = ''
    for i in range(6):
        hex += hexadecimal_digits[randint(0, 15)]
    return hex
