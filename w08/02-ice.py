"""
Lesson 02 ICE - Calling Functions
CSE 111
Author: [Your Name Here]
Description:

Practice calling built-in functions and standard library functions.

Instructions:

Write a program that:

1. Asks the user to enter a sentence.
   - Prints the length of the sentence.
   - Prints the sentence in uppercase.
   - Prints the sentence in lowercase.
   - Prints the number of words in the sentence. 
     (Hint: Use .split() and len())

2. Asks the user to enter a number.
   - Prints the square root of the number.
   - Prints the number rounded to 2 decimal places.
   - Prints the absolute value of the number.

3. (Stretch) Ask for two numbers and check if they are 
   close using math.isclose() with abs_tol=0.01.

"""

# Import necessary module
import math

# Step 1: Ask the user to enter a sentence
# TODO: Get user input
sentence = input("Type a sentence: ")
# TODO: Print length of sentence
length = len(sentence)
print(length)
# TODO: Print sentence in uppercase
print(sentence.upper())
# TODO: Print sentence in lowercase
print(sentence.lower())
# TODO: Print number of words in the sentence
count = 0
for word in sentence.split():
    count += 1
print(count)


# Step 2: Ask the user to enter a number
# TODO: Get user input and convert to float
number = float(input("Enter a decimal number: "))
# TODO: Print square root (be sure to use abs() first if needed)
number = abs(number)
print(math.sqrt(number))
# TODO: Print number rounded to 2 decimal places
print(f"{number:.2f}")
# TODO: Print absolute value of the number
print(abs(number))

# (Stretch) Step 3: Ask for two numbers and check if they are close
# TODO: Get two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# TODO: Use math.isclose() to compare them

if math.isclose(num1, num2, abs_tol = 0.01) == True:
    print("True")
else:
    print("False")
# TODO: Print whether they are close
