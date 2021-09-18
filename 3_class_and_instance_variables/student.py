"""
Student.py
20210917
ProjectFullStack
"""


class Student:

    # class variable to track the number of students
    # that exist
    student_count = 0

    def __init__(self, name, age, student_id, courses):
        """Constructor for the Student class"""
        self.name = name
        self.age = age
        self.student_id = student_id
        self.courses = courses

        # When adding a student, increment the
        # class variable student_count
        Student.student_count += 1


joe = Student('Joe', 18, 8429, ["MATH401", "COMP505"])
print("Created Joe!")
print("joe.student_count = ", joe.student_count)
print("Total student count is now: ", Student.student_count)

jane = Student('Jane', 20, 2931, ["HIST420", "COMP505"])
print('-------')
print("Created Jane!")
print("joe.student_count = ", joe.student_count)
print("jane.student_count = ", jane.student_count)
print("Total student count is now: ", Student.student_count)
#
#
Student.student_count += 1
print('-------')
print("Manually changed student count!")
print("joe.student_count = ", joe.student_count)
print("jane.student_count = ", jane.student_count)
print("Total student count is now: ", Student.student_count)


