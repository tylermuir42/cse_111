"""
Lesson 03 ICE - Writing and Calling Functions
CSE 111
Author: [Your Name Here]
Description:

Practice writing and calling a function that takes a string parameter and returns a result.

Instructions:

Write a program that:
  1. Contains a main() function that:
     - Asks the user to enter a singular noun (e.g., dog, party, box)
     - Calls make_plural(word) to compute the plural form of the word.
     - Prints the plural form.
  2. Contains one user-defined function:
     - make_plural(word): returns the plural version of the word.
       - If the word ends with 'y' --> replace 'y' with 'ies'
       - If the word ends with 's', 'x', 'z', 'ch', or 'sh' --> add 'es'
       - Otherwise --> add 's'
  3. make_plural should not include an input statement (keep that in main()).
     make_plural should not print anything. It should return a string.
  4. Only main() should print.
  5. Include a call to main() at the bottom of the file.
  6. Stretch #1 - Enhance your make_plural function to also handle words that end
     in 'f' and 'fe'.
       - If the word ends with 'f' --> replace 'f' with 'ves'
       - If the word ends with 'fe' --> replace 'fe' with 'ves'
  7. Stretch #2 - Handle irregular plural words, such as child, man, woman, mouse, 
     goose, tooth, foot, and any others you can think of. (Hint: make a 
     dictionary to handle these irregular words).  
"""

# Define the main function.
def main():
    # TODO: Ask the user to enter a singular noun.
    singular_noun = input("Enter a singular noun: ")

    # TODO: Call make_plural and store the result.
    plural_noun = make_plural(singular_noun)

    # TODO: Print the plural form.
    print(plural_noun)

# Define make_plural function.
def make_plural(word):
    """Return the plural form of the given word."""
    # TODO: Implement the pluralization rules.
    if word[-1] == 'y':
        word = word[:-1] + 'ies'
    elif word[-1] in ['s', 'ch', 'x', 'z', 'sh']:
         word = word + "es"
    elif word[-2:] in ['ch', 'sh']:
        #could also use word.endswith("ch")
        word = word + "es"
    else:
       ...

    return word

# Start this program by calling the main function.
main()
