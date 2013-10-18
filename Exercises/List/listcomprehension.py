a = [1, 2, 3, 3, 5, 9, 6, 2, 8, 5, 2, 3, 5, 7, 3, 5, 8]
b = []
print [b.append(item) for item in a if item not in b]
