from random import randint


def get_cmyk():
    return '{}%, {}%, {}%, {}%'.format(randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
