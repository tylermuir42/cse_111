import csv

#Index Constants
INUMBER_INDEX = 0
NAME_INDEX = 1

def main():
    student_list = read_dictionary("students.csv", INUMBER_INDEX)

    while True:
        i_number = input("Enter a student's i-number: (or 'quit'): ")
        if i_number == "quit":
            break

        #replace dashes with nothing
        new_number = i_number.replace("-", "")

        #check length
        if len(new_number) < 9:
            print("Number is too short")
        elif len(new_number) > 9:
            print("Number is too long")
        elif new_number.isdigit() == False:
            print("Do not enter letters")
        
   
        if new_number in student_list:
            print(student_list[new_number])
            print()
        else:
            print("Student not found")
            print()

def read_dictionary(filename, key_col):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    dictionary1 = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_col]
                dictionary1[key] = row_list

    return dictionary1

if __name__ == "__main__":
    main()