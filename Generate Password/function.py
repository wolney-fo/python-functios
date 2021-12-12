from random import randint


def generate_password(len=12):
    characters = '''0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[]^_`{çÇ}~'''
    password = ''
    for i in range(len):
        password += characters[randint(0, 93)]
    return password
