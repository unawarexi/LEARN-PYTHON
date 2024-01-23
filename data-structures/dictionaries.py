"""
a dictioninary is used 
a dictionary uses "{}" as brackets
"""


students = {"name": 'john',"age":25, "courses":['math', 'english', 'geology']}
print(students.get("course", "Not_Found"))

"""
use the .get method to display value of "none" instead of error 
this is useful when you make a mistake by requesting a  key that doesn't exist
the not found would display if it doesn't find any matching key
"""


# ======================== ADDDING and removing A VALUE TO THE DICTIONARY ==================
"""
you add value by using the update() method
you remove usinf del or pop 
  NOTE: the pop removes it from the dict but displays it as a new value
"""
colledge = {"name": 'john',"age":25, "courses":['math', 'english', 'geology']}
colledge.update({"name": "elisha", "phone": '555-55', "age":29})

age = colledge.pop("age")
print(age) #this explains the pop() method

print(colledge)

"""
this is looping throung the dictionary to get both the keys and the values
"""
for key, value in colledge.items():
    print(key, value)