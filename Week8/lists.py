# LISTS are changeable, ordered collections of items.
# They can contain different data types and can be nested.
# # Example of a list

fruits = ["apple", "banana", "cherry"]
# print(fruits[0])

# fruits[1] = "blueberry"  # Change the second item
# print(fruits)


# # Adding items to a list
# fruits.append("orange")  # Add an item to the end
# print(fruits)

# fruits.insert(1, "kiwi")  # Insert an item at a specific position
# print(fruits)

# Removing items from a list
fruits.remove("banana")  # Remove an item by value  
print(fruits)

# Sorting a list
fruits.sort(reverse=True)  # Sort the list in descending order
print(fruits)