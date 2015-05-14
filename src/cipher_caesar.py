#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "decpare"
__version__ = "1.0"

import os, sys, time
from alphabet import *

# ----------------------------- #

def encrypt(input_text, shift, abc, second_abc, formatting, save_case):
    if shift == "" or shift == 0: return input_text
    if save_case == False: input_text = list(str(input_text).lower())

    abc_len = len(abc)
    second_abc_len = len(second_abc)

    output_text = ""
    
    for s in input_text:
        s_lower = s.lower()

        if s in abc:
            output_text += abc[(abc.index(s) + shift) % abc_len]
        elif s_lower in abc:
            output_text += abc[(abc.index(s.lower()) + shift) % abc_len].upper()
        elif s in second_abc:
            output_text += second_abc[(second_abc.index(s) + shift) % second_abc_len]
        elif s_lower in second_abc:
            output_text += second_abc[(second_abc.index(s.lower()) + shift) % second_abc_len].upper()
        else:
            if formatting == True:
                output_text += s

    return output_text

def decipher(input_text, shift, abc, second_abc, formatting, save_case):
    if shift == "" or shift == 0: return input_text
    if save_case == False: input_text = list(str(input_text).lower())

    abc_len = len(abc)
    second_abc_len = len(second_abc)

    output_text = ""
    
    for s in input_text:
        s_lower = s.lower()

        if s in abc:
            output_text += abc[(abc.index(s) - shift) % abc_len]
        elif s_lower in abc:
            output_text += abc[(abc.index(s.lower()) - shift) % abc_len].upper()
        elif s in second_abc:
            output_text += second_abc[(second_abc.index(s) - shift) % second_abc_len]
        elif s_lower in second_abc:
            output_text += second_abc[(second_abc.index(s.lower()) - shift) % second_abc_len].upper()
        else:
            if formatting == True:
                output_text += s

    return output_text

if __name__ == "__main__":
    mode = input("Enter mode - encrypt or decipher (e/d): ")

    if mode != "e" and mode != "d": 
        print("Uncorrect command! Please close the program (Ctrl+Z) and restart it...")

    path_input_text = input("Enter path to input text: ")
    path_output_text = input("Enter path to output text: ")

    rus_key = input("Enter key for Russian alphabet: ")
    eng_key = input("Enter key for English alphabet: ")

    shift = int(input("Enter shift: "))
    
    save_case = input("Save case (y/n): ")

    if save_case == "y": 
        save_case = True 
    else:
        save_case = False

    formatting = input("Save formatting (y/n): ")

    if formatting == "y": 
        formatting = True 
    else:
        formatting = False

    input("Press any key for begin process...")

    begin = time.time()

    input_text = open(path_input_text, encoding = "utf-8").read()
    output_text = open(path_output_text, "w", encoding = "utf-8")
    
    if mode == "e": 
        output_text.write(encrypt(input_text, shift, rus_alphabet, eng_alphabet, True, save_case))
    elif mode == "d":
    	output_text.write(decipher(input_text, shift, rus_alphabet, eng_alphabet, True, save_case))
    else:
    	print("Uncorrect input 'mode'...")
