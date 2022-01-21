# /Task 1 Write a program that does the following:
import random
# a) Stores a random number (1-10) in a variable – see hint below.
number = random.randint(1,10)
# b) Asks a user for their name and stores this in a variable.
myName =input("Hello! what is your name?")
print("Well, "+ myName + "I am thinking of a number between 1 and 10.")
# c) Asks a user to guess the number between 1 and 10.
guess =int(input("guess a the number"))
# d) Tells the user whetherthey have guessed correctly.
if guess ==number:
     print("Good guess" + myName +"Welldone you guess my number" )

# Note: 
# import: Import all to import random
# Import: import allow you to ask user for fo an input and store that input in a variable
# int- int has been casted outside, so when we ask user any number it will be integer short for int
# iteration- we use loop in line 10 to iterate and run through a particular code until specific contion is met, in the case, in line 10 we set a condition to guess number , if guess condition is met, print Good guess + myname + welldone
# translate to js
#python:  import random ::   js: 
#replace the colon : that indicate the beginning of a code block by { in js

