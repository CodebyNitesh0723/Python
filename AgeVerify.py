# Set a secret age (this is the number you’ll compare the user’s input with).
# Ask the user to enter their age.
# Try to convert the input into a number:
#     If it’s not a valid number (like if the user types letters), show an error message like “Please enter a valid number.”
# If the input is a number:
#     Check if it's a float (has a decimal) or an integer.
#     If the age is equal to the secret age, print “You’re awesome!”
#     If the age is less than the secret, print “You’re too young!”
#     If the age is greater than the secret, print “You’re too wise!”
#     Also tell the user whether they entered a float or an integer.


import random, fractions, sys, math

print('Welcome to the Age Verifier Program where i challenge you to verify my age.')
while True:
    while True:
        secret_age = random.randint(30, 75)
        user_input = input("Enter your age:\n")
        if user_input.isalpha() and not user_input.isdigit():
            print('Please enter a valid number.\n')
        # elif  any(char.isalpha() or char in '@`#$%^&*()_=[]{}<>~' for char in user_input):
        #     print("Please enter a valid number.\n")
        #     continue
        else:
            break

    if '.' in user_input:
        user_input = int(float(user_input))
        print('You enter Float number.')
    elif '/' in user_input:
        user_input = int(fractions.Fraction(user_input))
        print('You enter Decimal number.')
    else:
        user_input = int(user_input)
        print('You enter Integer.')

    if user_input == secret_age:
        print('You are awesome. You choose the correct secret age. My secret age is:', secret_age)
        sys.exit()

    elif user_input < secret_age:
        print('You are too below in guessing my age.  \n')
    else:
        print('You are too high in guessing my age.\n')












