# 1. Below The Arithmetical Mean
# When given a list, the program should return a list of all the elements below the original
# list’s arithmetical mean. The arithmetical mean is the sum of all elements divided by the
# number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

def belowMean(arr):
    lessThan = []
    arrMean = sum(arr)/len(arr)
    for i in arr:
        if (i < arrMean):
            lessThan.append(i)
    return lessThan

print(belowMean([1, 3, 5, 6, 4, 10, 2, 3]))

# 2. Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

def twoLowest(arr):
    lowestTwo = []
    arr.sort()
    lowestTwo.append(arr[0])
    lowestTwo.append(arr[1])
    return lowestTwo

print(twoLowest([198, 3, 4, 9, 10, 9, 2]))