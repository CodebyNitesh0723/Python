# # Debugging Unit Chapter
# def box_print(symbol, width, height):
#     if len(symbol) != 1:
#         raise Exception('Symbol must be a single character string.')
#     if width <= 2:
#         raise Exception('Width must be greater than 2.')
#     if height <= 2:
#         raise Exception('Height must be greater than 2.')
#
#     print(symbol * width)
#     for i in range(height - 2):
#         print(symbol + (' ' * (width - 2)) + symbol)
#     print(symbol * width)
#
#
# try:
#     box_print('*', 4, 4)  # ✅ OK
#     box_print('O', 20, 5)  # ✅ OK
#     box_print('x', 1, 3)  # ❌ Width too small (<= 2)
#     box_print('ZZ', 3, 3)  # ❌ Symbol is more than 1 character
# except Exception as err:
#     print('An exception happened: ' + str(err))
# try:
#     box_print('ZZ', 3, 3)
# except Exception as err:
#     print('An exception happened: ' + str(err))

# 1. ✅ Assertions — Sanity Checks  Debugging
# ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
# ages.sort()
# # ages.reverse()
# # ages
# # [15, 17, 22, 26, 47, 54, 57, 73, 80, 92]
# assert ages[0] <= ages[-1]  # Assert that the first age is <= the last age

# ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
# ages.reverse()
# # ages
# # [73, 47, 80, 17, 15, 22, 54, 92, 57, 26]
# assert ages[0] <= ages[-1]  # Assert that the first age is <= the last age.

# 2. 🧾 Logging — Better Than print() Debugging

# import logging
#
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.debug('Start of program')
#
#
# def factorial(n):
#     logging.debug('Start of factorial(' + str(n) + ')')
#     total = 1
#     # for i in range(n + 1):  # ❌ Bug is here
#     for i in range(1, n + 1):  # Fixed Bug is here
#         total *= i
#         logging.debug('i is ' + str(i) + ', total is ' + str(total))
#     logging.debug('End of factorial(' + str(n) + ')')
#     return total
#
#
# print(factorial(5))
# logging.debug('End of program')


# example to understand why debug is better than print

# USING LOGGING.DEBUG TO RUN THE PROAGRAM
# import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# logging.disable(
#     logging.CRITICAL)  # WHEN THIS LINE IS ENABLE THEN IT disables all logging messages, including critical ones

# def process_data(data):
#     logging.debug("Processing started")
#     if not data:
#         logging.error("No data to process")
#         return None
#     total = sum(data)
#     avg = total / len(data)
#     logging.info(f"Average is: {avg}")
#     return avg
#
#
# process_data([10, 20, 30])
# process_data([])

# Debug messages are clear and structured
# You can keep all logs hidden from the user
# You can export logs to a file for review

# USING PRINT TO RUN PROGRAM
# def process_data(data):
#     print("Processing started")
#     if not data:
#         print("ERROR: No data to process")
#         return None
#     total = sum(data)
#     avg = total / len(data)
#     print("Average is:", avg)
#     return avg
#
#
# process_data([10, 20, 30])
# process_data([])

# User sees "ERROR: No data to process"
# In large applications, that error may get lost in 1000s of lines
# No log history, timestamps, or severity level

#
# # how you can log messages to a file instead of printing them in the terminal.
# import logging
#
# # Set up logging to write to a file called 'process_log.txt'
# logging.basicConfig(
#     filename='process_log.txt',  # <-- Log file name
#     level=logging.DEBUG,  # <-- Log everything from DEBUG and above
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )
#
#
# def process_data(data):
#     logging.debug("Processing started")
#     if not data:
#         logging.error("No data to process")
#         return None
#     total = sum(data)
#     avg = total / len(data)
#     logging.info(f"Average is: {avg}")
#     return avg
#
#
# process_data([10, 20, 30])
# process_data([])
# # Optional: Disable logging after this point
# logging.disable(logging.CRITICAL)


# 🧠 Mu’s Debugger – Mastering Interactive Debugging
# print('Enter the first number to add:')
# first = input()
# print('Enter the second number to add:')
# second = input()
# print('Enter the third number to add:')
# third = input()
# print('The sum is ' + first + second + third)


# 🎯 Breakpoints – Pausing Your Program Where You Want

#
# heads = 0
# for i in range(1, 1001):
#     if random.randint(0, 1) == 1:
#         heads += 1
#     if i == 500:
#         print('Halfway done!')
#
# print('Heads came up', heads, 'times.')
# breakpoint_test.py

# def add_numbers(a, b):
#     result = a + b  # <- Set a breakpoint here
#     return result
#
#
# def main():
#     x = 10
#     y = 20
#     sum = add_numbers(x, y)
#     print(f"The sum of {x} and {y} is {sum}")  # <- And maybe set a breakpoint here
#
#
# if __name__ == "__main__":
#     main()


# Practice Program: Debugging Coin Toss
# import random
#
# guess = ''
# while guess not in ('heads', 'tails'):
#     print('Guess the coin toss! Enter heads or tails:')
#     guess = input()
#     toss = random.randint(0, 1)  # 0 is tails, 1 is heads
#     if toss == guess:
#         print('You got it!')
#     else:
#         print('Nope! Guess again!')
#     guess = input()
#     if toss == guess:
#         print('You got it!')
#     else:
#         print('Nope. You are really bad at this game.')

# Fix code
#
# import random
#
# guess = ''
# while guess not in ('heads', 'tails'):
#     print('Guess the coin toss! Enter heads or tails:')
#     guess = input().lower()  # Normalize input to lowercase
#
# toss = random.randint(0, 1)  # 0 is tails, 1 is heads
# toss_result = 'heads' if toss == 1 else 'tails'  # Convert toss to string
#
# if toss_result == guess:
#     print('You got it!')
# else:
#     print('Nope! Guess again!')
#
#     # Second guess with validation
#     guess = ''
#     while guess not in ('heads', 'tails'):
#         print('Enter heads or tails:')
#         guess = input().lower()
#
#     if toss_result == guess:
#         print('You got it!')
#     else:
#         print('Nope. You are really bad at this game.')
