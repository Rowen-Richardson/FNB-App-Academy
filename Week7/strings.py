# File: strings.py
# Strings are a sequence of characters enclosed within either single or double Quotes

message = 'Hello world'

# print(message)

#Advanced concepts of strings
# Indexing(-1, 0, 1 ,2)
# print(message[-1]) # Output: d
# print(message[0])  # Output: H
# print(message[1])  # Output: e
# print(message[2])  # Output: l
# print(len(message))  # Output: 11

print(message.strip()) #Removes leading and trailing whitespace
print(message.lower()) #Converts to lowercase
print(message.upper()) #Converts to uppercase
print(message.replace('world', 'Python'))  # Replaces 'world' with 'Python
