#-------------------------------------------------------------------------------
# Name:       Week 14
# Purpose:    Integer Detector
#
# Author:     Liam Musgrove
#
# Created:    05/03/2026
#-------------------------------------------------------------------------------


def readposint():
    while True: #I did have a tiny bit of help from Google on this part to aid me in my troubleshooting, I needed a hint on how to make a program repeat forever.

        try:
            num = int(input("Please give me a positive integer! "))

            if num > 0: #If the integer is more than zero
                print("{0} is a positive integer!".format(num))
                
            if num < 0: #If the integer is less than zero.
                print("{0} is a negative integer!".format(num))
                
        except: #If the user's input is not a valid integer, it will throw up this message.
                print ("That's not an integer!")

            
        
    

    


   



readposint()


        
