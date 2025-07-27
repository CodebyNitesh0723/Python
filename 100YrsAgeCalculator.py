# Create a program that asks the user for their full name, age, and current year. Then calculate and display the year when they will turn 100 years old.
import time

print('\n')
print("Welcome to my 100 years age calculating program.")
name = input("Can you type your Full Name please. ")
age = input("Can you type your Age please.\n ")
date = input("Can you type current year please.\n ")

if name == '':
    print('Please type your Full Name please.')
else:
    print("Calculating your date when you will reach 100 years old...")
    time.sleep(5)
year_hundred = 100 - int(age)
date_hundred = int(date) + int(year_hundred)
age = str(date_hundred)
print("Hi " + name + "," + " " + " You will reach 100 years old in " + age + " years.")
