# @ DEBUGGING LOGGING PRACTICAL CODE FROM THIS CHAPTER

# Create a function add(x, y) that returns the sum.
# Use logging.debug() to log the start and end of the function.
# Log the result with logging.info().

# import logging
#
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logging.debug('Program Started')
#
#
# def add(x, y):
#     logging.debug('Program Adding')
#     return x + y
#
#
# logging.debug('The result is ' + str(add(1, 2)))
# logging.debug('Program Ended')
# import logging
#
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logging.debug('Program Started')
#
#
# def add(x, y):
#     logging.debug(f'Starting add({x}, {y})')  # Log function start
#     result = x + y
#     logging.info(f'Result of add({x}, {y}) is {result}')  # Log result as info
#     logging.debug(f'Ending add({x}, {y})')  # Log function end
#     return result
#
#
# add(1, 2)
#
# logging.debug('Program Ended')


# @Check for Input Errors
# Create a function divide(x, y) that divides two numbers.
# If y is 0, log an error.
# Otherwise, log the result using info.

# import logging
#
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger('Program started')
# logging.disable(logging.CRITICAL)  # enable this code to disable all log console for user
#
# def divided(x, y):
#     logging.debug(f'Dividing number divided ({x}, {y})')
#     if y != 0:
#         logging.debug('Program does not have any issue')
#         result = x / y
#         logging.debug(f'The result of dividing divided({x}, {y}) is  {result}\n')
#
#     else:
#         logging.error(f'Dividing number is divided({y})')
#         logging.error(f'{y} cannot be used to divided any number')
#
#
# divided(10, 2)
# divided(10, 0)
# logging.debug('Program Ended')


# @Log to File

import logging

logging.basicConfig(filename='mylog.txt', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Program Started')
logging.info('Welcome to program where output is save in file not show in terminal\n')


def add(x, y):
    result = x + y
    if y == 0:
        logging.error('Please give some another number expect 0')
    else:
        logging.info(f'Adding {x} to {y}')
        logging.info(f'The result of adding {x} and {y} is {result}')


add(x=int(input('First Number: ')), y=int(input('Second Number: ')))
logging.info('Program ended')
# add(10, 2)
