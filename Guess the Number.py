# The Goal: Similar to the first project, this project also uses the random module in Python.
# The program will first randomly generate a number unknown to the user. 
# The user needs to guess what that number is. (In other words, the user needs to be able to input information.) 
# If the user’s guess is wrong, the program should return some sort of indication as to how wrong (e.g. The number is too high or too low). 
# If the user guesses correctly, a positive indication should appear. 
# You’ll need functions to check if the user input is an actual number, to see the difference between the inputted number and the randomly generated numbers, and to then compare the numbers.
# Concepts to keep in mind:
# •	Random function
# •	Variables
# •	Integers
# •	Input/Output
# •	Print
# •	While loops
# •	If/Else statements

from random import randint

print("Welcome To The Number Guessing Game.\n")
while True:
    right_number = randint(1,100)
    count = 0
    try:
        guess = int(input("Guess The Number : "))
    except:
        print("Please Enter the Number only!!!")
        continue

    while True:
        if guess < right_number:
            print("Too Low!!!")
            try:
                guess = int(input("Try Again : "))
                count += 1
            except:
                print("Please Enter the Number only!!!")
                continue
        elif guess > right_number:
            print("Too High!!!")
            try:
                guess = int(input("Try Again : "))
                count += 1
            except:
                print("Please Enter the Number only!!!")
                continue
        elif guess == right_number:
            print(f"Yah, You Won \n You Guess the right number after the {count} try. ")
            break
        else:
            print("You may be entered the wrong number.")
    
    ch = input("Do You Want to Guess Again (Yes/No) : ")
    if 'y' in ch.lower():
        continue
    else:
        print("Thanks for Playing this Game. :) \nGood Bye.")
        break

