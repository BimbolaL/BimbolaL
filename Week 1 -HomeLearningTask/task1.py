# /Task 1 Write a program that does the following:
import random
# a) Stores a random number (1-10) in a variable – see hint below.
number = random.randint(1,10)
# b) Asks a user for their name and stores this in a variable.
myName =input("Hello! what is your name?")
# c) Asks a user to guess the number between 1 and 10.
guess =int(input("guess a the number"))
# d) Tells the user whetherthey have guessed correctly.
if guess == number:
     print("Good guess" + myName +"Welldone you guess my number" )