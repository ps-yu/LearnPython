"""
Class and instance attributes
# Instance attributes are invoked when a new object is created
# Class attributes are the attributes defined within the class and are also invoked during object creation
# Class attributes are usually constants and have global scopes
"""


# class Student:
#     # Class attributes
#     school = "TMU"
#     location = "Toronto"
#
#     # Instance attributes
#     def __init__(self, name, student_id):
#         self.name = name
#         self.student_id = student_id
#
#     def get_student_info(self):
#         print(f"{self.name} is a student in {Student.school} which is located in {Student.location}")
#
#
# s1 = Student("John Doe", 12134)
# s1.get_student_info()

# Methods and static methods in python
# Static methods are the methods that don't use the self keywords and are instances of the class rather than the objects

# class Student:
#     # Class attributes
#     school = "TMU"
#     location = "Toronto"
#
#     # Instance attributes
#     def __init__(self, name, student_id):
#         self.name = name
#         self.student_id = student_id
#
#     def get_student_info(self):
#         print(f"{self.name} is a student in {Student.school} which is located in {Student.location}")
#
#     @staticmethod
#     def average(num1, num2, num3):
#         return (num3+num2+num1)/3
#
#
# s1 = Student("John Doe", 12134)
# s1.get_student_info()
#
# print(s1.average(12, 3, 5))

""" Principles of OOP
Abstraction and Encapsulation in python
# Abstraction -: Hiding the implementation details of a class and only showing the essential features to the users
# Encapsulation -: Wrapping data and function into a single unit(object)
"""









