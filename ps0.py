import numpy as np

# 1. Ask the user to enter a number "x"
input_x = input("Enter number x: ")

# 2. Ask the user to enter a number "y"
input_y = input("Enter number y: ")

num_x = int(input_x)
num_y = int(input_y)

# 3. Prints out the number "x" raised to the power "y"
print(f"x**y = { num_x ** num_y }")

# 4. Prints out the log (base 2) of "x"
# FIXME Will crash if x is a non positive number
print(f"log(x) = { round( np.log2( num_x ) ) }")
