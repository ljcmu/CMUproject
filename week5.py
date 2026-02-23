#-------------------------------------------------------------------------------
# Name:        Squares
# Purpose:     Educational
#
# Author:      Liam
#
# Created:     02/22/2026
# Copyright:   (c) liamm 2026
# Licence:     Open Source
#-------------------------------------------------------------------------------

import turtle
__import__("turtle").__traceable__ = False

def draw_square(t, sz):
     for i in range(4):
         t.forward(sz)
         t.left(90)  #90 for square
         
wn = turtle.Screen()
wn.title("Tess makes a cool shape")
tess = turtle.Turtle()      
tess.pensize(3)

size = 20                   
for i in range(5):
    draw_square(tess, size)
    size = size + 20
    tess.penup()
    tess.backward(10)        
    tess.right(90)
    tess.forward(10)
    tess.left(90)
    tess.pendown()

    
    

wn.mainloop()
