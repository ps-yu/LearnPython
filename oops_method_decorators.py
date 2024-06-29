# class method decorator
# It is used to modify or change the attributes that are associated with the class

class Student:
    class_room = "ENG101"

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.class_room = Student.class_room

    def display_info(self):
        return self.name, self.class_room, self.student_id

    # To change the attributes once the object has already been instantiated
    def change_instance_object_class(self, new_class_room):
        self.class_room = new_class_room

    @classmethod
    def change_class_room(cls, name):
        cls.class_room = name

    @property
    def change_class_automatically(self):
        return self.class_room


# s1 = Student("John", "101")
# print(s1.display_info())
# s1.change_class_room("SLC102")
# print(Student.class_room)
# print(s1.display_info())
# Since the student object is invoked first with the ENG101 class room it will not change
# But the class_room attribute of the Student class has been changed
# s2 = Student("Doe", "521212")
# print(s2.display_info())
# print(Student.class_room)
# To change the classroom of the student created at the first place (s1)
# a method can be created in the student class
# s1.change_instance_object_class("PSY101")
# print(s1.display_info())
# print(Student.class_room)
# There is another way of doing the same
s1 = Student("John", "101")
print(s1.display_info())
s1.class_room = "SLC1002"
print(s1.display_info())


