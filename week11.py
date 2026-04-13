#-------------------------------------------------------------------------------
# Name:       Week 11
# Purpose:    Line Reversal
#
# Author:     Liam Musgrove
#
# Created:     04/12/2026
#-------------------------------------------------------------------------------


myfile = open("kulltext.txt", "w")
myfile.write("This is the class I am taking with teacher John Kull!")
myfile.close()

f = open("kulltext.txt", "r")
xs = f.readlines()
f.close()


g = open("newkulltext.txt", "w")
for v in xs:
    g.write(v[::-1])     #I asked AI about the reverse command, I needed to refresh my memory on it to help me write my program
g.close()
