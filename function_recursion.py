"""
Function is a block of statement that performs a specific task
Syntax: def function(param1, param2...):
python does not use {}. indentation is important to define the block of the code
"""

# def greatest_number(input_list):
#     req_number = 0
#     for i in input_list:
#         if i > req_number:
#             req_number = i
#     return req_number
#
#
# list1 = [1, 4345, 54, 54, 64342, 54, 23, 52]
# print(greatest_number(list1))
# Create a function to find the average of three numbers
# def cal_average(x=1, y=2, z=3):
#     return ((x+y+z) / 3)
# print(cal_average(12,3,4))


"""
Default parameters in functions
If there is a function call with no arguments and default parameters is defined in the function
then the function is invoked with those arguments
"""


# print(cal_average())
# Recursion
# When a function calls itself repeatedly
# Write a function to find the factorial of a given number

# def find_factorial(number):
#     factorial = number
#     while not number == 1:
#         number -= 1
#         factorial *= number
#     return factorial
#
#
# # Using recursion
# def factorial_using_recursion(number):
#     if number <= 1:
#         return 1
#     else:
#         return number * factorial_using_recursion(number - 1)
#
#
# print(find_factorial(6))
# print(factorial_using_recursion(6))
