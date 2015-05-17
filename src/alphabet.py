#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "decpare"
__version__ = "1.0"

# ----------------------------- #


def create_user_alphabet(key, input_alphabet):
    if key == "":
        return input_alphabet
    # thanks python.su - paranax
    # if use 'set' the list is sorted
    key = [e for i, e in enumerate(key) if e not in key[:i]]

    for i in range(len(key)):
        key[i] = key[i].lower()
        if key[i] in input_alphabet:
            del input_alphabet[input_alphabet.index(key[i])]

    return key + input_alphabet

eng_alphabet = list("abcdefghijklmnopqrstuvwxyz")
rus_alphabet = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
user_alphabet = ""

if __name__ == "__main__":
    user_alphabet = create_user_alphabet("danil", eng_alphabet)
    print(user_alphabet)
