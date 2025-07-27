import sys
import time

print('\n')
print(
    "Hi,  Welcome to my Software which count the number of words you used in your input Sentences, it characters and how many Vowels and Consonants letters you use. So, Stay Turn.\n")
special_chars = "!@#$%^&*()_+={}[]:;<>?,./\"'"
Vowel = "a, e, i, o, u, A,E,I,O,U"

while True:
    User_input = input("Enter your Sentence: ")

    if User_input.strip() == '' or all(char in special_chars for char in User_input):
        print('Please type your Sentence please.\n')

    else:
        word = len(User_input.split())
        Word = str(word)

        cha = len(User_input.replace(" ", ""))
        CHA = str(cha)

        print("Counting the number of Words  in your sentences....")
        time.sleep(4)
        print("You Have " + Word + "  Words in your Sentence.\n")

        print("Counting the number of characters in your sentences....")
        time.sleep(5)
        print("You Have " + CHA + "  characters in your Sentence.\n")

        print("Counting the number of Vowel Letters in your sentences....")
        time.sleep(2)

        vowel_count = consonants_count = 0
        for letter in User_input:
            if letter in Vowel:
                vowel_count += 1
            else:
                consonants_count += 1
        count_consonants = str(consonants_count)
        count_vowel = str(vowel_count)
        print("You Have " + count_vowel + "  Vowel letters in your Sentence.\n")

        print("Counting the number of consonants Letters in your sentences....")
        time.sleep(2)
        print("You Have " + count_consonants + "  consonants letters in your Sentence.\n")
        time.sleep(0.5)
    print('Thank you For using my program ')
    sys.exit()
