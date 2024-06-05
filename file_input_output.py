"""
Python can be used to perform operations on a file (read and write data)
Python can be used to read and write data both in binary and text files
"""

# Open, read and close a file
# if the mode is not defined it is read by default
# f = open("file_name", "mode")
# f = open("demo.txt", "r")
# # to read the data from the file
# data = f.read()
# print(data)
# print(type(data))
# # close the file after it's usage
# f.close()

"""
Different modes/operation for files in python
"r" reading data from a file
"w" open for writing, truncating the file (overwrite the previous characters)
"x" creating a new file and open it for writing
"a" open the file for writing and appending to the end of the file if it exists
"b" binary mode
"t" text mode(default)
"+" open a disk for updating
"""
# read method
# f.read(5) defines to read 5 characters in the file
# f.readline() reads the file one line at a time

# f = open("demo.txt", "r")
# line = f.readline()
# print(line)
# line2 = f.readline()
# print(line2)
# line3 = f.readline()
# print(line3)
# f.close()
# f = open("demo.txt", "w")
# f.write("New data will be added and the old data will be lost")
# f.close()
"""File operation using with syntax"""
# with open("demo.txt", "a+") as f:
#     f.write("\n Write one more line to the file")
#     print(f.read())
#     f.close()
"""Deleting a file in python"""
# deleting a file in python is done using os module
# with open("demo2.txt", "a+") as f:
#     f.write("this is will create a new file and append data in the file")
#     print(f.read())
#     f.close()

# import os
# os.remove("demo2.txt")

"""Write a function that will replace every occurance of java with python in a file called language.txt"""


# with open("language.txt", "a+") as f:
#     f.write("Java is a beginner friendly language. \nJava can be used for multiple purposes such as backend "
#             "development as well as data science.")
#     f.close()
#
# def write_data(file):
#     with open(file, "r") as f:
#         data = f.read()
#     new_data = data.replace("Java", "Python")
#     with open(file, "w") as f:
#         f.write(new_data)
#
#
# write_data("language.txt")
