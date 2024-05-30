"""
Dictionaries and Sets
"""

"""
Dictionaries in python is similar to objects in javascript
Dictionaries are used to store the data values in key:value pairs
Dictionaries are unordered, mutable and cannot have duplicate keys
"""
# Example of creating and mutating  dictionary in python

# dict1 = {"name": "python", "version": 3.12, "is_easy": True, 4: 34}
# change_language = input("please enter the name of the new language: ")
# dict1["name"] = change_language
# print(dict1)

# Nested Dictionaries
# dict2 = {
#     "dict3": dict1,
# }
# print(dict2["dict3"]["name"])
"""
useful dictionaries methods
dict.values() - returns all the values stored in the dictionary
dict.keys() - returns all the keys stored in the dictionary
dict.items() - return all the key value pair as tuples
dict.get("key") - returns the value of the provided key. if no such key exists it returns None instead of error
dict.update({city: toronto}) add new key-value pair to the existing dictionary
"""

"""
sets in python is the collection of unordered items
each item in the set are unique and they are immutable
lists and dictionaries cannot be stored in the sets because they are mutable
tuples can be passed in the sets because they are immutable
"""

# nums1 = {1, 2, 3, 4, 5}
# nums2 = set()     #empty set
# print(nums2)

"""
Useful methods in sets
Sets are mutable but the elements in the sets must be immutable
set.add(el)
set.remove(el)
set.clear() #Empty the set
set.pop() #removes a random value
set.union(set2) #combines both set values and returns a new set
set.intersection(set2) #combines common values nad returns new
"""































