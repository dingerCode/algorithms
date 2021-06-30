# 1. Compute the sum of digits in all numbers from 1 to n. When a user enters a number
# n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15
def sumOfDigits(num):
    return (num * (num + 1)) / 2

print(sumOfDigits(5))


# 2. Find max number from 3 values, entered manually from a keyboard.
# Example: 124, 21, 32. Result = 124.
def maxNum(n1, n2, n3):
    return max(n1, n2, n3)

# without built-in functions
def max_num(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return
    return c

print(maxNum(124, 21, 32))
print(max_num(124, 21, 32))


# 3. Count odd and even numbers. Count odd and even digits of the whole number.
# Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd
# digits (3 and 5).
def oddEvenCount(n):
    odds = 0
    evens = 0

    while n != 0:
        current_digit = n % 10
        if current_digit % 2:
            odds += 1
        else:
            evens += 1
        n = n // 10

    return ["Evens: " + str(evens), "Odds: " + str(odds)]

print(oddEvenCount(34560))