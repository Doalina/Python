import re
import os

CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", 'i', "ji", "g")


TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def normalize(name):
    file_name, file_extention = os.path.splitext(name)
    translated_name = ''
    pattern = r'[a-zA-Z0-9]'
    for symbol in file_name:
        if re.search(pattern, symbol) != None:
            translated_name += symbol
        elif ord(symbol) in TRANS:
            translated_name += TRANS[ord(symbol)]
        else:
            translated_name += '_'

    return translated_name + file_extention