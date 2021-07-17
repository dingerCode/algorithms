# 1. Below The Arithmetical Mean
# When given a list, the program should return a list of all the elements below the original
# list’s arithmetical mean. The arithmetical mean is the sum of all elements divided by the
# number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

def below_mean(arr):
    less_than = []
    arr_mean = sum(arr)/len(arr)
    for i in arr:
        if (i < arr_mean):
            less_than.append(i)
    return less_than

print(below_mean([1, 3, 5, 6, 4, 10, 2, 3]))

# 2. Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

def two_lowest(arr):
    arr.sort()
    return arr[:2]

print(two_lowest([198, 3, 4, 9, 10, 9, 2]))