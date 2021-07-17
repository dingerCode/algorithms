# 1. Even First
# Your input is an array of integers, and you have to reorder its entries so that the even entries
# appear first. You are required to solve it without allocating additional storage (operate with
# the input array).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

def evens_first(arr):
    zero = 0
    for i in range(len(arr)):
        if arr[zero] % 2 != 0:
            t = arr[zero]
            arr.remove(arr[zero])
            arr.append(t)
        else:
            zero += 1
    return arr

print(evens_first([7, 3, 5, 6, 4, 10, 3, 2]))

# 2. Increment a Number
# Write a program that takes as input an array of digits encoding a nonnegative decimal
# integer D and updates the array to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].

def num_increment(arr):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i - 1] += 1
    else:
        if arr[0] == 10:
            arr[0] = 1
            arr.append(0)
    return arr

print(num_increment([1, 2, 9]))
print(num_increment([9, 9, 9]))