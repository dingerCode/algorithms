from itertools import permutations

# 1. Reverse a Statement
# Build an algorithm that will print the given statement in reverse.
# Example: Initial string = Everything is hard before it is easy
# Reversed string = easy is it before hard is Everything

def stringReversal(s):
    wordList = s.split()
    wordList.reverse()
    reversedSentence = " ".join(wordList)
    return reversedSentence


print(stringReversal('Everything is hard before it is easy'))

# 2. Permutations
# Write a solution that will print all permutations of a string.
# A permutation is an act of changing the arrangement of characters.
# Example: String = ABC, Return {ABC, ACB, BAC, BCA, CBA, CAB}

def strPerm(s):
    perm = [''.join(p) for p in permutations(s)]
    return perm


print(strPerm('ABC'))

# 3. Count Characters
# Create a program that will count vowels and consonants in a string.
# Example: String = “hello world”, Return {Vowels: 3, Consonants: 7}

def countChars(s):
    vowels = 0
    consonants = 0
    lowerStr = s.lower()
    for i in lowerStr:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            vowels += 1
        elif (i != " "):
            consonants += 1
    return f'Vowels: {vowels}, Consonants: {consonants}'


print(countChars("hello world"))