test_data = [10, 100, 20, 90, 30, 80, 40, 70, 50, 60]
print(test_data)

# 1. Selection Sort
# Implement the selection sort algorithm that is sorting in descending order.
def selection_sort(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr

print(selection_sort(test_data))

# 2. Bubble Sort
# Implement the bubble sort algorithm that is sorting in descending order.
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort(test_data))

# 3. Insertion Sort
# Implement the insertion sort algorithm that is sorting in descending order.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort(test_data))



