# Task 2 
# Write a program that asks a user for their favourite number between 1 and 100 
# 
# 
# and then tells them a joke based on the number. You should use a minimum of 3 jokes.
# Write a program that asks a user for their favourite number between 1 and 100 
import random 
myName = input("Hello! What is your name?")
favNum = random.randint(1,100)
print("Well, " + favNum + ",I am thinking of a number between 1 and 100.")
jokes =int("Hello! what is your favorite number?")
# and then tells them a joke based on the number. You should use a minimum of 3 jokes.
if favNum == 50:
     print(" Why is six scared of seven? Because seven, eight, nine!" )
elif favNum > 50:
    print("Why were the two fours skipping lunch? They already eight" )
else:
    favNum < 50
    print("Why can you never call a bee with a phone? The signal is always buZZy.")

# Note: 
# line 7: Import random library for favorite number
# Input: input allow you to ask user for an input and store that input in a variable
# name variable was created, 
# line 9- here we call the favourite number and store value in the number, randint function is provided by random module randint() 
# Import: import allow you to ask user for an input and store that input in a variable
# int- int has been casted outside, so when we ask user any number it will be integer short for int
# condition- we use several lines to compare two values with a comparison operator and evaluate it to Boolean value
#  line 13 -19 the condition fav == 50 is false , equal equal( ==) sign i used in expresion to see where favNum is equal to 50.
#13-19 because the condition  on line 13, line 15 is not met  it goes to else

