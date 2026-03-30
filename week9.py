#-------------------------------------------------------------------------------
# Name:       E-finder
# Purpose:    Finding the number of words and the letter "e" in a string
#
# Author:      Liam Musgrove
#
# Created:     03/29/2026
# Copyright:   
# Licence:     Open Source
#-------------------------------------------------------------------------------


import string

import math

mytext = """
Yesterday
All my troubles seemed so far away
Now it looks as though they're here to stay
Oh, I believe in yesterday
Suddenly
I'm not half the man I used to be
There's a shadow hangin' over me
Oh, yesterday came suddenly
Why she had to go, I don't know, she wouldn't say
I said something wrong, now I long for yesterday
Yesterday
Love was such an easy game to play
Now I need a place to hide away
Oh, I believe in yesterday
Why she had to go, I don't know, she wouldn't say
I said something wrong, now I long for yesterday
Yesterday
Love was such an easy game to play
Now I need a place to hide away
Oh, I believe in yesterday
Mm mm mm mm mm mm mm """  # "Yesterday" by The Beatles, Copyright 1965

textlength=len(mytext)

def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

wds = remove_punctuation(mytext).split()

def count_e(text):
    count = 0
    for c in text:
        if c == "e":
            count += 1
    return(count)



epercent = (count_e(mytext) / textlength) * 100





print(f" This text has {textlength} words and has the letter e exactly {(count_e(mytext))} times which is {epercent} percent of the text.")
