# Private attributes and methods in python
# Private attribute in python is implemented differently than Java
# Private methods and attributes are only accessible within the class internally
# implemented using "__""


class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.__balance = balance

    def __printBalance(self):
        return self.__balance

    def setBalance(self, new_balance):
        self.__balance = new_balance
        print(self.__printBalance())


# s1 = BankAccount("John", "32323", 6500)
# in the following implementation method print balance and the attribute __balance
# is not directly available with the object
# the only way to access and change the values is through the other methods defined within the class
# s1.setBalance(4500)


# Inheritance -: Same concept as Java
# when one class derives the properties and methods of another class
# The following is the demo of inheritance the polymorphism


class Toyota:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def start(self):
        print(self.name + " has started with normal engine ")


class Lexus(Toyota):
    def __init__(self, name, color, hp):
        # Calling the constructor from the super class
        super().__init__(name, color)
        self.hp = hp

    # Python does not require the explicit use of override keyword to indicate method overriding
    def start(self):
        print(self.name + " is a powerful car with " + str(self.hp))


car1 = Lexus("RS", "white", 800)
car1.start()


# Inheritance in python can be single inheritance, multi-level inheritance or multiple inheritance
# Mutliple inheritance in python
class A:
    varA = "welcome to class A"


class B:
    varB = "welcome to class B"


class C(A, B):
    varC = "welcome to class C"


c1 = C()
print(c1.varA, c1.varB, c1.varC)

