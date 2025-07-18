"""
Lesson 04 ICE - Functions with Parameters
CSE 111
Author: [Your Name Here]
Description:

Practice writing functions with parameters using the exercises below

Instructions:
Complete each of the functions below.
"""
# 1. Simple Calculator Functions
# Write functions for the basic math operations: add, subtract, multiply, 
# and divide. Each function should take two parameters (numbers) and 
# return the result.

def add(a, b):
    # Your code here
    return a + b

def sub(a, b):
    # Your code here
    return a - b

def mult(a, b):
    # Your code here
    return a * b

def div(a, b):
    # Your code here
    return a / b

# Example Usage:
print(add(5, 3))  # Should print 8
print(sub(5, 3))  # Should print 2
print(mult(5, 3)) # Should print 15
print(f"{div(5,3):.2f}")   # Should print 1.67


# 2. String Repeater
# Write a function `repeat_string` that takes two parameters: a string and 
# an integer `n`.
# The function should return the string repeated `n` times.

def repeat_string(string, n):
    # Your code here
    return string * n

# Example Usage:
print(repeat_string("Hello", 3))  # Should print "HelloHelloHello"
print(repeat_string("Bob", 5)) # Should print "BobBobBobBobBob"

# 3. Calculate Compound Interest
# Write a function `compound_interest` that calculates compound interest based on
# principal, rate, and time (in years). Use the formula: A = P * (1 + r)**t.

def compound_interest(principal, rate, time):
    # Your code here
    return principal * ((1 + rate)**time)

# Example Usage:
print(compound_interest(1000, 0.05, 5))  # Should return the total amount after 5 years


# 4. Password Validator
# Write a function `validate_password` that takes a password (string) as a parameter.
# Check if the password meets the following criteria:
# - At least 8 characters
# - Contains both letters and numbers
# Return True if valid, False otherwise.

def validate_password(password):
    # Your code here
    digit = False
    length = False
    letter = False
    
    if any(char.isdigit() for char in password):
        digit = True
    if any(char.isalpha() for char in password):
        letter = True
    if len(password) >= 8:
        length = True
    if length == True and digit == True and letter == True:
        return True
    else:
        return False

# Example Usage:
print(validate_password("pass1234"))  # Should return True
print(validate_password("pass"))      # Should return False


# 5. Calculate Distance Between Two Points
# Write a function `calculate_distance` that takes four parameters:
# x1, y1, x2, y2 representing the coordinates of two points.
# Calculate and return the distance between these points using the formula:
# distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2).

import math
def calculate_distance(x1, y1, x2, y2):
    # Your code here
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Example Usage:
print(calculate_distance(1, 2, 4, 6))  # Should return the distance between 
                                       # points (1, 2) and (4, 6), which is 5.0