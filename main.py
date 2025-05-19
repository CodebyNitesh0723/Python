# print("Hello")
# print("What is your Name ?")
# MyName= input()
# print("It is good to meet you " +  MyName)
# print("The length of you full name is:")
# print(len(MyName))
# print("What is you age?")
# age = input()
# print("You will be " + str(int(age) + 1 ) + "  years old in next year.")

# name = input("Enter your name: ")
# age = 3000
# if name == 'Alice':
#     print('Hi, Alice.')
# elif age < 12:
#     print('You are not Alice, kiddo.')
# elif age > 2000:
#     print('Unlike you, Alice is not an undead, immortal vampire.')
# elif age > 100:
#     print('You are not Alice, grannie.')

# #If else
# spam = 0
# if spam < 5:
#     print('Hello, world.\n')
#     spam = spam + 1
#
# # While loop statement
# spam = 0
# while spam < 5:
#     print('Hello, world.')
#     spam = spam + 1

# An ann yoing whiile loop
# name = ''
# while name != 'your name':
#     print('Please type your name.')
#     name = input()
# print('Thank you!')

# Break Statemen to stop loop
# while True:  # repeat forever
#     print("What’s the secret word?")
#     name = input()
#     if name == "your name":  # if correct
#         break                # manually stop
# print("Thank you!")


# Continue Statement

# while True:
#     print('Who are you?')
#     name = input()
#
#     # If the name is not 'Joe', skip the rest of the loop and go back to the start.
#     if name != 'Joe':
#         continue
#
#     print('Hello, Joe. What is the password? (It is a fish.)')
#     password = input()
#
#     # If the password is 'swordfish', break out of the loop.
#     if password == 'swordfish':
#         break
#
# print('Access granted.')

# Another condition exampele
# name = ''
# while not name:
#     print('Enter your name:')
#     name = input()
#
# print('How many guests will you have?')
# numOfGuests = int(input())
#
# if numOfGuests:
#     print('Be sure to have enough room for all your guests.')
# print('Done')
# Step 1: Ask for the user's name
name = ''
# while not name:
#     print('Enter your name:')
#     name = input()
#
# # Step 2: Ask for the number of guests and validate the input
# while True:
#     print('How many guests will you have?')
#     try:
#         numOfGuests = int(input())  # Try to convert the input to an integer
#         if numOfGuests > 0:
#             break  # If the input is valid (greater than 0), exit the loop
#         else:
#             print('Please enter a valid number of guests (greater than 0).')
#     except ValueError:
#         print('Please enter a valid number (not text).')
#
# # Step 3: If the input is valid, print the message
# print('Be sure to have enough room for all your guests.')
# print('Done')

# for Loops and the range() Function
# print('My name is')
# for i in range(5):
#     print('Nitesh Five Times (' + str(i) + ')')

#An Equivalent while Loop
# print('My name is')
# i = 0
# while i < 5:
#     print("Nitesh Five Times (" + str(i) + ')')
#     i = i + 1
#

# The Starting, Stopping, and Stepping Arguments to range()
# for i in range(0, 10, 2):
#     print(i)
#
    # The range() function can also be called with three arguments. The first two arguments will be the start and stop
    # values, and the third will be the step argument. The step is the amount that the variable is increased by after each iteration.
    # So calling range(0, 10, 2) will count from zero to eight by intervals of two.


# Importing Modules
# A module in Python is like a toolbox that contains special tools (functions).
# Python comes with many such toolboxes — this is called the standard library.
#
# Examples:
#     math module — has math tools like square root, pi, etc.
#     random module — has tools to create random numbers.
#     time module — has tools to work with time and delays.

# Why Import a Module?
#     Before you use the tools in a module, you must open the toolbox — this is done using the import keyword.
#    Once imported, you can use all the functions inside it.
# For example :
# import random
# for i in range(5):
#     print(random.randint(1, 10))

# # Ending a Program Early with the sys.exit() Function
# import sys
#
# while True:
#     print('Type exit to exit.')
#     response = input()
#     if response == 'exit':
#         sys.exit()
#     print('You typed ' + response + '.')

# 🔹 Case 1: Using import sys + sys.exit()
# import sys
#
# while True:
#     response = input("Type 'exit' to quit: ")
#     if response == 'exit':
#         sys.exit()
#     print("You typed:", response)
#
# print("This will NOT run if sys.exit() is called.") # When the user types 'exit', sys.exit() immediately ends the whole program.
# This will never run — because the program completely stops.

#  Case 2: Using break instead of sys.exit()

# while True:
#     response = input("Type 'exit' to quit: ")
#     if response == 'exit':
#         break
#     print("You typed:", response)
#
# print("This WILL run after the loop ends.")
# When the user types 'exit', break will only stop the loop — not the entire program.
# This  does run, because the program keeps going after the loop ends.

