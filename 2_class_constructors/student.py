"""
Student.py
20210917
ProjectFullStack
"""

class Student:
    """
    Class representing a student.

    Public properties:
        - Name - str
        - Age - int
        - Student Id - int
        - Registered Courses - list of str
    """

    def __init__(self, name, age, student_id, courses):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.courses = courses


joe = Student('Joe', 18, 8429, ["MATH401", "COMP505"])
print(joe.name)
print(joe.age)
print(joe.student_id)
print(joe.courses)

jane = Student('Jane', 20, 2931, ["HIST420", "COMP505"])
print(joe.name)
print(joe.age)
print(joe.student_id)
print(joe.courses)
