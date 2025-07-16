# Example of a creating a Student data type

# Define a Student class
class Student:

    # This function is called whenever an "instance" of the class
    # is created. It initializes the newly created object.
    def __init__(self, given_name, family_name, phone_number, student_id, major):
        self.given_name = given_name      # Attribute for the student's first name
        self.family_name = family_name    # Attribute for the student's last name
        self.phone_number = phone_number  # Attribute for the student's phone number
        self.student_id = student_id      # Attribute for the student's ID
        self.major = major                # Attribute for the student's major

    # Return the student's details
    def get_info(self):
        return f"{self.given_name} {self.family_name}\n" + \
               f"Phone: {self.phone_number}\n" + \
               f"Student ID: {self.student_id}, Major: {self.major}"

    # Change student's major
    def change_major(self, major):
        self.major = major

    def __str__(self):
        return f"{self.family_name}, {self.given_name}: {self.major}"

def main():
    # Create instances of the Student class
    string1 = "dkfsjsdlkjf"
    list1 = [1,2,3,4,55]

    student1 = Student("Charlie", "Daniels", "208-555-5555", "I-12345678", "Computer Science")
    student2 = Student("Diana", "McMurphy", "801-555-5555", "I-543231232", "Software Engineering")

    print(student1)
    print(student2.get_info())

    students = {}
    students[student1.student_id] = student1
    students[student2.student_id] = student2

    print()

    while True:
        print("Enter the next student's info:")
        fname = input("First name: ")
        if fname == "done":
            break
        lname = input("last name: ")
        phone = input("Phone: ")
        inumber = input("inumber: ")
        major = input("Major: ")

        new_student = Student(fname, lname, phone, inumber, major)
        # students.append(new_student)
        students[new_student.student_id] = new_student 


    for key, value in students.items():
        print(value.get_info())
        print("-"*20)


    print(students['I-12345678'].get_info())


    

if __name__ == "__main__":
    main()