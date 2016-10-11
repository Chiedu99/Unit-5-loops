#Chiedu Nduka-Eze Unit 5 10/10/16
#This program prompts the user for a guess between 1-100

import random

def askUser():
    """This function asks the user if they want to play the game"""
    while True:
        answer = input("Do you want to play chiedu's amazing game?")
        if answer == "yes":
            return True
        elif answer == "no":
            return False

def randomNumber():
    """This function generates a random number"""
    number = random.randint(1,100)
    return number

def userGuess():
    """This function makes sure the guess is between 1 and 100"""
    while True:
        guess = int(input("What is your guess?:"))
        if guess >= 1 and guess <= 100:
            return guess

def tellUser(guess,number):
    """This function tells the user if their number is too small or too big. It also tells them if they are correct"""
    if guess > number:
        print("you are incorrect, the number is lower!")
        return True
    elif guess < number:
        print("you are incorrect. the number is greater!")
        return True
    else:
        print("You are correct!!!!")
        return False




def main():
    while askUser():
        numberOfGuesses = 1
        number = randomNumber()
        guess = userGuess()
        while tellUser(guess,number):
            numberOfGuesses += 1
            guess = userGuess()
        print("you tried",numberOfGuesses, "time(s)")




main()
