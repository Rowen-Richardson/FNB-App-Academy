# Exception handling allows a programmer to handle errors gracefully without crashing the program.
# It is used to catch and handle exceptions that may occur during the execution of a program.
'''try:
   print(x)
except NameError:   # Catching a specific exception
   print("Variable x is not defined.")
except Exception as e:  # Catching any other exception
   print(f"An error occurred: {e}")'''

# try:
#    print(x)
# except:
#    print("Something went wrong.")
# finally:
#    print("The 'try except' block is finished.")

try:
    print(x)
except NameError:
    print("Variable x is not defined.")
except:
    print("Everything went wrong.")

x = -2

if x < 0:
    raise Exception("Sorry, no numbers below zero")