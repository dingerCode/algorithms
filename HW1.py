# 1. Compute the sum of digits in all numbers from 1 to n. When a user enters a number
# n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15
def sumOfDigits(num):
    result = 0
    if num != 0:
        for i in range(1, num + 1):
            result += i
    print(result)

sumOfDigits(5)

# 2. Find max number from 3 values, entered manually from a keyboard.
# Example: 124, 21, 32. Result = 124.
def maxNum(n1, n2, n3):
    highest = max(n1, n2, n3)
    print(highest)

maxNum(124, 21, 32)

# 3. Count odd and even numbers. Count odd and even digits of the whole number.
# Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd
# digits (3 and 5).
def oddEven(n):
    evenNums = []
    oddNums = []
    while (n > 0):
        rem = n % 10
        if (rem % 2 == 0):
            evenNums.append(rem)
        else:
            oddNums.append(rem)
        n = int(n / 10)
    print("Even Numbers : ", evenNums)
    print("Odd Numbers : ", oddNums)

oddEven(34560)