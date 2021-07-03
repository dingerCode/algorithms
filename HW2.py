from collections import Counter

# 1. Split in Half
# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the
# second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

def splitInHalf(str):
    dividedLength = round(len(str)/2)
    str1 = str[:dividedLength]
    str2 = str[dividedLength:]
    return str2 + str1


print(splitInHalf("bbbbbcaaaaa"))
print(splitInHalf('aabb'))


# 2. Unique Characters in String.
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.

def uniqueChars(str):
    return len(str) == len(set(str))

print(uniqueChars('abcde'))
print(uniqueChars(('aabcde')))