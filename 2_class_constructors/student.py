"""
Student.py
20210917
ProjectFullStack
"""

class Student:
    """
    Class representing a student.

    Public properties:
        - name - str
        - age - int
        - student_id - int
        - courses - list of str
    """

    def __init__(self, name, age, student_id, courses):
        """Constructor for the Student class"""
        self.name = name
        self.age = age
        self.student_id = student_id
        self.courses = courses


joe = Student('Joe', 18, 8429, ["MATH401", "COMP505"])  # <__main__.Student object at 0x00000230DA8BE130>
print(joe.name)
print(joe.age)
print(joe.student_id)
print(joe.courses)

jane = Student('Jane', 20, 2931, ["HIST420", "COMP505"])  # <__main__.Student object at 0x00000230DAA1A040>
print(jane.name)
print(jane.age)
print(jane.student_id)
print(jane.courses)

jane.name = 'askdjhasdkjhlasd'
print(jane.name)
