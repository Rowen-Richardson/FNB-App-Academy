# TUPLE a collection of objects that are ordered and immutable
# Tuples can contain different data types and can be nested.

# Example of a tuple
my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple[0])  # Accessing the first item
print(my_tuple)
print(my_tuple[0])  
print(my_tuple[3]) 

# Concatenating tuples(combining two tuples)
tuple1 = (6, 7, 8)
tuple2 = (9, 10)

combined_tuple = tuple1 + tuple2
rep_tuple = tuple1 * 3  # Repeating the first tuple twice
print(combined_tuple)  # Output: (6, 7, 8, 9, 10)
print(rep_tuple)  # Output: (6, 7, 8, 6, 7, 8, 6, 7, 8)