#-------------------------------------------------------------------------------
# Name:       Week 7
# Purpose:    Time Converter
#
# Author:      Liam
#
# Created:     03/08/2026
#-------------------------------------------------------------------------------

import math

import sys

def to_secs(h, m, s):      # This is the converter.
    return h * 3600 + m * 60 + s

def test(did_pass):        # This is how the system will test.
    """  This will tell us if the test is successful.  """
    linenum = sys._getframe(1).f_lineno   
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)          # This tells us if the test was successful or not.
    


test(to_secs(2, 30, 10) == 9010)
test(to_secs(2, 0, 0) == 7200)
test(to_secs(0, 2, 0) == 120)
test(to_secs(0, 0, 42) == 42)
test(to_secs(0, -10, 10) == -590)



    
