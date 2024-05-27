def min_max(arr):
    return min(arr), max(arr)

numbers = [3, 6, 1, 9, 4, 8]
min_val, max_val = min_max(numbers)
print("Minimum Value:", min_val)
print("Maximum Value:", max_val)