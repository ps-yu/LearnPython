"""
OOPS in python
Object oriented is the fundamental of programming and increases code reusability
The four basic of OOPS are abstraction, encapsulation, inheritance and polymorphism
"""
"""
Class is a blue print for creating objects
# creating a class
class Student:
    name = "John Doe"
# creating object (instance)
s1 = Student()
print(s1.name)
"""


# Creating constructor for the classes
# self parameter is used to refer the current instance of the class
# Python does not allow constructor overloading like java or other programming languages
# The bottom most constructor will over-ride the all constructors above  itself
# Therefore the following code will not work


# class Car:
#     def __init__(self):
#         self.name = None
#         self.year = None
#         self.color = None
#         print("Object invoked without any properties")
#
#     def __init__(self, name, year, color):
#         self.name = name
#         self.year = year
#         self.color = color
#
#     def get_properties(self):
#         print(self.name)
#         print(self.year)
#         print(self.color)
#
#
# # s1 = Car("Nissan", "2012", "white")
# # s1.get_properties()
# s2 = Car()

# In python constructor over-loading is performed with some tricks
# Example of constructor over-loading using default method
class Car:
    def __init__(self, name, year, color):
        self.name = name
        self.year = year
        self.color = color

    @classmethod
    def from_name(cls, name):
        return cls(name, None, None)

    def get_properties(self):
        print(f"Name: {self.name}")
        if self.year:
            print(f"Year: {self.year}")
        if self.color:
            print(f"Color: {self.color}")


# Example usage:

s1 = Car("Nissan", "2012", "white")
s1.get_properties()
s2 = Car.from_name("Toyota")
s2.get_properties()
