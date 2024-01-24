set1 = {1, 2, 3}
set2 = {2, 3, 5}
set3 = {2, 5, 6}

# Eliminate elements from set1 that are in both set2 and set3
set1.difference_update(set2.intersection(set3))

print(set1)  # Set1 will now contain elements {2, 3}