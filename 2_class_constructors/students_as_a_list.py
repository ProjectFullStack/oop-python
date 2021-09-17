"""
Lets represent a group of students as a list
Each student will have the following attributes:
    - Name - str
    - Age - int
    - Student Id - int
    - Registered Courses - list of str
        - The courses that this student is registered for
"""

# I can do this using a list
students = [
    ['Joe', 18, 8429, ['MATH401', 'COMP505']],
    ['Jane', 20, 2931, ['HIST420', 'COMP505']],
    ['Bob', 35, 1923, []]
]

joe = students[0]
print(joe[0])  # print joe's name
print(joe[1])  # print joe's age
print(joe[2])  # print joe's student id
print(joe[3])  # print joe's courses
