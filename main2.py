# def hello():
#     print('Howdy!')
#     print('Howdy!!!')
#     print('Hello there.')
# print(hello())

# def hello(name):
#     print('Hello, ' + name)
#
# hello('Alice')
# hello('Bob')

# The call Stack
# def greet():
#     print("Hello!")
#
# def say_name():
#     greet()
#     print("My name is Nitesh")
#
# def main():
#     say_name()
#
# main()


# Bitwise  Operators
# a = 60 # 0011 1100
# b = 13 # 0000 1101
#
# print(a & b) # 12 (0000 1100)
# print(a | b) # 61 (0011 1101)
# print(a ^ b) # 49 (0011 0001)
# print(~a) # -61 (1100 0011)
# print(a << 2) # 240 (1111 0000)
# print(a >> 2) # 15 (0000 1111)

# THE LOCAL AND GLOBAL VARIABLE
# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)
#
#
# def bacon():
#     ham = 101
#     eggs = 0
#
# spam()
#
# # The Global Statement
# eggs = 'global'
# def spam():
#     global eggs      # Step 3: use the global variable 'eggs'
#     eggs = 'spam'    # Step 4: change it to 'spam'
#
#      # Step 1: create a global variable 'eggs' with value 'global'
# spam()               # Step 2: call the spam() function
# print(eggs)          # Step 5: print the global 'eggs', now changed to 'spam'
print(dir(__builtins__))
