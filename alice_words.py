#-------------------------------------------------------------------------------
# Name:        alicewords
# Purpose:
#
# Author:      Liam
#
# Created:     5/15/2026
#-------------------------------------------------------------------------------

# I was not able to complete this assignment. I was able to write some bits of code
# based off the ones in the book but I was not able to get anything to work.
# I figured I would just turn in some of my broken code rather than nothing because
# a couple of points is better than none at all.










def splitstring():
    f = open("alice.txt")
    content = f.read()

    words = content.split()
    word_counts = {}
    for word in f:
        word_counts[letter] = word_counts.get(word00000000, 0) + 1



def alicefunc():
    while True:
        f = open("alice.txt", "r")
        content = f.readlines()
        if len(content) == 0:
            break
        f.close()
        wordcount = {}
        for word in content:
            wordcount[word] = wordcount.get(word, 0) + 1
            worditem = list(wordcount.items())
            worditem.sort()
            print(list(worditem))


def newalicefunc():
    f = open("alice.txt", "r")
    xs = f.readlines()
    f.close()

    xs.sort()
    xs.count(ord)

    g = open("alicewords.txt", "w")
    for v in xs:
        g.write(v)
    g.close()



def loadwords():
    f = open("alice.txt", "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds






















































    















newalicefunc()
