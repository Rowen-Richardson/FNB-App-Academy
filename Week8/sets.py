# SETS are unordereed collections of unique elements.
# They are useful for membership testing and eliminating duplicates.

my_set = {1, 2, 3, 4, 5}
print(my_set)

# Adding elements to a set
my_set.add(6)
print(my_set)

# Removing elements from a set
my_set.remove(2)
print(my_set)

# Checking membership
print(3 in my_set)
print(2 in my_set)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
print(set1 | set2)

# Intersection
print(set1 & set2)

# Difference
print(set1 - set2)
 