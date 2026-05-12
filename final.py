#-------------------------------------------------------------------------------
# Name:       Week 16 FINAL PROJECT
# Purpose:    Number Guessing Game
#
# Author:     Liam Musgrove
#
# Created:    05/11/2026
#-------------------------------------------------------------------------------


import random # Can't hurt to have these!
import turtle
import math

def testeasy(): # The three test functions below are meant to test the individual modes to ensure functionality.
    assert gamelogiceasy()

def testhard():
    assert gamelogichard()

def testsecret():
    assert supersecret()


def highscorecount(): # This code checks for the "lastscore.txt" file on the disk and displays it upon opening the program. If it does not exist, the game will assume this is your first time playing and leave you a friendly message.
    try:
        f = open("lastscore.txt")
        content = f.read()
        f.close()
        words = content
        print((words))
    except:
        print("Looks like this is your first time playing. Have fun!")

    

def menu():
    print("Hello and welcome to my game show, Numbermania!")

def giveoptions():
        response = input("Type 1 then Enter to play regular mode, 2 then Enter for hardcore mode! ")
        if response == '1': # This starts easy mode.
            gamelogiceasy()
        elif response == '2': # This starts hard mode.
            gamelogichard()
        elif response == 'supersecret': # Ooh, I wonder what this does...?
            secretmode()
        else:
            print("That's not an option, silly!")
            print(" ")
            giveoptions() # If the user gives an invalid input, it restarts the program.

def gamelogiceasy(): # This is the easiest mode. The player must guess a random number between 1 and 50.
    rng = random.Random()
    answer = rng.randrange(1, 51)
    tries = 0
    while True:
        try:
            tries += 1
            playeranswer = int(input("I'm thinking of a number between 1-50. What do you think it is? ")) # Everything below this code handles the user input. This program can handle anything from integers to letters or nothing at all.
            if playeranswer < answer: # If the player's answer is lower than the correct answer, it will display this.
                print("Incorrect! Try higher.")
                print(" ")
            elif playeranswer > answer: # If the player's answer is higher than the correct answer, it will display this.
                print("Incorrect! Try lower.")
                print(" ")
            else: # If the player's answer is correct, it will end the game session ask the player what to do next.
                print("Congratulations, you found the number!")
                print(" ")
                break
        except: # This handles the exception that occurs if the user inputs something other than an integer. Without this, the game will crash.
            print("Invalid answer, try again!")

    print("\n\nGreat, you got it in {0} guesses!\n\n".format(tries))
    myfile = open("lastscore.txt", "w") # This code writes the score of your attempt to a .txt file for the program to read the next time you start the game.
    myfile.write("You beat your last attempt in {0} tries!\n".format(tries))
    myfile.close()
    postresponse = input("Press 1 then Enter to play again, 2 then Enter to try your hand at hardcore mode, any other key to quit! ") # This code gives the player a choice of playing on easy, hardcore, or exiting the game.
    if postresponse == '1':
        gamelogiceasy()
    elif postresponse == '2':
        gamelogichard()
    elif postresponse == 'supersecret':
        secretmode()

def gamelogichard(): # This is the hard mode. It essentially uses the same code as easy mode, except the range of answers is much wider.
    rng = random.Random()
    answer = rng.randrange(1, 501)
    tries = 0
    while True:
        try:
            tries += 1
            playeranswer = int(input("I'm thinking of a number between 1-500. What do you think it is? "))
            if playeranswer < answer:
                print("Incorrect! Try higher.")
                print(" ") # The blank space here prints in between the "Incorrect!" message and the next answer prompt to clear screen clutter.
            elif playeranswer > answer:
                print("Incorrect! Try lower.")
                print(" ")
            else:
                print("Congratulations, you found the number!")
                print(" ")
                break
        except:
            print("Invalid answer, try again!")

    print("\n\nGreat, you got it in {0} guesses!\n\n".format(tries))
    myfile = open("lastscore.txt", "w")
    myfile.write("You beat your last attempt in {0} tries!\n".format(tries))
    myfile.close()
    postresponse = input("Press 2 then Enter to play again, 1 then Enter to take down the difficulty a notch, or any other key to quit! ")
    if postresponse == '1':
        gamelogiceasy()
    elif postresponse == '2':
        gamelogichard()
    elif postresponse == 'supersecret':
        secretmode()

def secretmode(): # The super secret mode, should you find it, requires the player to find the correct number between 1 and 1000000.
    rng = random.Random()
    answer = rng.randrange(1, 1000001)
    tries = 0
    print("Congratulations, you found the super secret mode!")
    print (" ")
    while True:
        try:
            tries += 1
            playeranswer = int(input("I'm thinking of a number between 1-1000000. What do you think it is? "))
            if playeranswer < answer:
                print("Incorrect! Try higher.")
                print(" ")
            elif playeranswer > answer:
                print("Incorrect! Try lower.")
                print(" ")
            else:
                print("Congratulations, you found the number!")
                print(" ")
                break
        except:
            print("Invalid answer, try again!")

    print("\n\nGreat, you got it in {0} guesses!\n\n".format(tries))
    myfile = open("lastscore.txt", "w")
    myfile.write("You beat your last attempt in {0} tries!\n".format(tries))
    myfile.close()
    postresponse = input("Press 3 then Enter to play the secret mode again, 1 then Enter for easy mode, or 2 then enter for hardcore mode! ")
    if postresponse == '1':
        gamelogiceasy()
    elif postresponse == '2':
        gamelogichard()

def startgame(): # This does what it says. It starts the game by running the three functions below at once.
    menu()
    highscorecount()
    giveoptions()

startgame()
