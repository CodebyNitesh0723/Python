# ROCK, PAPER, SCISSORS
# 0 Wins, 0 Losses, 0 Ties
# Enter your move: (r)ock (p)aper (s)cissors or (q)uit
# p
# PAPER versus...
# PAPER
# It is a tie!
# 0 Wins, 1 Losses, 1 Ties
# Enter your move: (r)ock (p)aper (s)cissors or (q)uit
# s
# SCISSORS versus...
# PAPER
# You win!
# 1 Wins, 1 Losses, 1 Ties
# Enter your move: (r)ock (p)aper (s)cissors or (q)uit
# q


import random, sys
print('Welcome to the Rock, Paper, and Scissors game!')
Wins = 0
Loses = 0
Ties = 0
while True:
    print(f'{Wins} Wins, {Loses} Losses, {Ties} Ties')
    while True:
        print('Choose your option from: Rock, Paper, Scissors')
        user_choice = input()
        new_user_choice =  user_choice.lower()
        if new_user_choice == 'q':
            sys.exit()
        else:
            if new_user_choice == 'r' or new_user_choice == 'p' or new_user_choice == 's':
                break
            print('Please Choose from Rock, Paper, or Scissors.')

    # Now when user type any then we nee to print what versus what so we use this if elif to do that
    if new_user_choice == 'r':
        print('Rock versus...')
    elif new_user_choice == 'p':
        print('Paper versus...')
    elif new_user_choice == 's':
       print('Scissor..')

    # Now it time for the computer chose where we use random.randint to get 3 random number and based on the random number we assign the r p or s
    com_number = random.randint(1, 3)
    if com_number == 1 :
        computer_choice = 'r'
        print('Computer chose Rock')
    elif com_number == 2 :
        computer_choice = 'p'
        print('Computer chose Paper')
    elif com_number == 3 :
        computer_choice = 's'
        print('Computer chose Scissor')

# Now if  user win or loose or tie with computer we have to show the output result so for that we are writing this code
    if new_user_choice == computer_choice:
        print('It is a Tie Game.')
        Ties += 1
    elif new_user_choice == 'r' and computer_choice == 's':
        print('You Loose!')
        Wins += 1
    elif new_user_choice == 'p' and computer_choice == 'r':
        print('You Win!')
        Wins += 1
    elif new_user_choice == 's' and computer_choice == 'p':
        print('You Losses!')
        Wins += 1
    elif new_user_choice == 'r' and computer_choice == 'p':
        print('You Looses!')
        Loses += 1
    elif new_user_choice == 'p' and computer_choice == 's':
        print('You Looses!')
        Loses += 1
    elif new_user_choice == 's' and computer_choice == 'r':
        print('You Looses!')
        Loses += 1




