"""
Difference between a json and a xml file
json :
{
"name" : "tom",
"address" : "1 python street"
"phone" : "127.0.0.1"
}

xml file
<name>tom</name>
<address> 1 python street </address>
<phone> 127.0.0.1 </phone>
"""
import json
# JSON stands for javascript object notation. It is a data exchange format similar to XML

book = {'tom': {
    'name': 'tom',
    'address': 'python street',
},
    'bob': {
        'name': 'tom',
        'address': 'python street',
    }}

# print(book)
# Converts dictionary object into a string
# s = json.dumps(book)
# print(s)

# Since json.dumps convert the dictionary object into a string, it can be written into another file for data exchange
# with open("./demo.txt", "w") as f:
#     f.write(s)

with open("./demo.txt", "r") as f:
    s = f.read()

# Converting string back to a dictionary
book2 = json.loads(s)

# Type of the object is string
print(type(s))
# Type of the object is dictionary
print(type(book2))
