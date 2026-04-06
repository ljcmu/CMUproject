#-------------------------------------------------------------------------------
# Name:       Replacement
# Purpose:    Replacing certaiin characters within a string with other characters
#
# Author:      Liam Musgrove
#
# Created:     04/05/2026
# Copyright:   N/A
# Licence:     Open Source
#-------------------------------------------------------------------------------


def replace(s, old, new):
    splithing = s.split(old)
    glue = (new)
    return glue.join(splithing)

    



print(replace("Mississippi", "i", "I"))

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
print(replace(s, "om", "am"))

print(replace(s, "o", "a"))



# I did use a tiny bit of help from AI for this assignment. I told the AI the desired results and used it to basically troubleshoot my code as it kept bringing up errors.





