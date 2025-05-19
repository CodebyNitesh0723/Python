# After completing Chapter 1 and Chapter 2 We should suppose to understand the logic about how to write a code to play a game called guess the number
# 1. Import random module
# 2. Generate a random number between 0 and 100
# 3. Set the number of attempts (e.g., 10)
# 4. Start a loop for a limited number of attempts
#     a. Prompt the user to input a guess
#     b. Check if the guess is correct, too high, or too low
#     c. Provide feedback
#     d. If correct, print a success message and exit the loop
# 5. If the player runs out of attempts, reveal the correct number and print a failure message
# 6. End the program
import sys
# import sys, math, random
# print("I am thinking of a number between 0 and 100. Can you able to guess the number? I challenge you. HAHA !! \n")
# real_number = random.randint(0, 100)
# print("secret number is: " + str(real_number))
# for guess_number in range(1, 35):
#     print("Take a guess.")
#     guess_number = int(input())
#     if guess_number < real_number:
#         print("Your guess is too low.\n")
#     elif guess_number > real_number:
#         print("Your guess is too high.\n")
#     else :
#         break
#
# if guess_number == real_number:
#     print('Good job! You guessed my number in ' + str(guess_number) + ' guesses!')
# else:
#     print('Nope. The number I was thinking of was ' + str(secretNumber))

from random import randint
secret_number = randint(1, 25)
print("I am thinking of a number between 0 and 25. Can you able to guess the number? I challenge you. HAHA !! \n")
for attempt  in  range (1, 6):
    guess_number = int(input("Guess the number: "))
    if guess_number < secret_number:
        print("You guessed my number is too low. \n")
        print("You have " + str(5 - attempt) + " attempts left. \n")
    elif guess_number > secret_number:
        print("You guessed my number is too high.")
        print("You have " + str(5 - attempt) + " attempts left. \n")
    else:
        break
if guess_number == secret_number:
    print('🎉 Good job! 🎉 You guessed my number in ' + str(attempt) + ' guesses! \n')
else:
    print("You are sucha noob. HAHA (L for Looser Y for You) You Fucking Looser")
    print('Nope. The number I was thinking of was ' + str(secret_number) + " 😞\n" )






