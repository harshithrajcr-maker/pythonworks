nested = [[1, 2], [3, 4], [5, 6]]

flattened = [num for s in nested for num in s]

print(flattened)
