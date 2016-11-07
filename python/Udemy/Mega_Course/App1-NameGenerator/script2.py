__author__ = 'eladron'

import random, string

#letter_input_1 = raw_input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
#letter_input_2 = raw_input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
#letter_input_3 = raw_input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")


#print(letter_input_1 + letter_input_2 + letter_input_3)


def generator(wordLength, numberOfWords):
    vowels     = "aeiou"
    consonants = "bcdfghjklmnopqrstvwxyz"
    anyLetter  = string.ascii_lowercase
    lsNames    = []
    name       = ''

    lsLetters = getUserInput(wordLength)

    for j in range(numberOfWords):
        for letter in lsLetters:
            if letter == 'v':
                letter = random.choice(vowels)
            elif letter == 'c':
                letter = random.choice(consonants)
            elif letter == 'l':
                letter = random.choice(anyLetter)

            name +=  letter

        lsNames.append(name)
        name = ''

    return lsNames

def getUserInput(wordLength):

    lsLetters = []

    for i in range(wordLength):
        inputLetter = raw_input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
        lsLetters.append(inputLetter)

    return lsLetters


print(generator(5, 10))