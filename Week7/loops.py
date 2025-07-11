# LOOPS = are an essential concept in programming that allow you to execute a block of code multiple times.
# They are used to automate repetitive tasks and iterate over collections of data.

# 1. For Loop
# A for loop is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects. 
# It executes a block of code for each item in the sequence.
# Example:
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     print(number)

# 2. While Loop
# A while loop continues to execute a block of code as long as a specified condition is true.
# Example:
# count = 1  # Initialize the count variable
# while count <= 5:
#     print(count)
#     count += 1  # Increment the count to avoid an infinite loop


# LOOPS CONTROL STATEMENTS
# Control statements in loops allow you to alter the flow of execution within the loop.
# 1. Break Statement
# The break statement is used to exit a loop prematurely when a certain condition is met.
# Example:
fruits = ["apple", "banana", "cherry", "date"]
# # This loop will print each fruit until it encounters "banana", at which point it will exit the loop.
# for fruit in fruits:
#      if fruit == "cherry":
#          break  # Exit the loop when "cherry" is found
#      print(fruit)

# # 2. Continue Statement
# # The continue statement skips the current iteration of the loop and moves to the next iteration.
# # Example:
# print()

# for fruit in fruits:
#      if fruit == "cherry":
#          continue  # Skip the iteration when "cherry" is found
#      print(fruit)

# # 3. Pass Statement
# # The pass statement is a null operation; it does nothing when executed. It is often used
# # as a placeholder in loops or conditionals where code will eventually go.
# print()
# # Example:
# for fruit in fruits:
#      if fruit == "cherry":
#          pass  # Do nothing when "cherry" is found
#      print(fruit)

count = 0  # Initialize the count variable
while count <= 5:
    if count == 3:
        break  # Exit the loop when count is 3
    print(count)
    count += 1  # Increment the count to avoid an infinite loop