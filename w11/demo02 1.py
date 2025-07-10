# Compound lists

students = [
    ["Alice", [85, 90, 78]],
    ["Bob", [92, 88, 84]],
    ["Charlie", [80, 70, 75]]
]


NAME_INDEX = 0
GRADES_INDEX = 1



# print(f"{students[2][NAME_INDEX]} - {sum(students[2][GRADES_INDEX]) / len(students[2][GRADES_INDEX])}")

# Calculate the average grade for each student
for student in students:  # ["Alice", [85,90,78]  ]
    name = student[NAME_INDEX] # student's name
    grades = student[GRADES_INDEX] # list of their grades
    average = sum(grades) / len(grades) # sum the list of grades
    print(f"{name}'s average grade is {average:.2f}")

# Add a new student named Deb
students.append(["Deb", [98, 99, 100]])
for student in students:
    print(student)






# students = [
#     ["Alice", [85, 90, 78]],
#     ["Bob", [92, 88, 84]],
#     ["Charlie", [80, 70, 75]]
# ]


# Add a new score to everyone
for student in students:
    student[GRADES_INDEX].append(100)

print(students)