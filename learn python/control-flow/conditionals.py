# using comparison operator 

# the "==" sign is used to denote direct in values comparison
# but the "is" is used to check if the both values is same everywhere
"""
e.g a = [1,2,3], b = [1,2,3]
 a == b # would give us true because the value is same 
 a is b # would not give us true because a is not b; it uses "id" to check

"""
language = "java"

if language == "python":
 print ("language is python")
elif language == "java":
    print ("language is java")
else:
    print ("language is unknown")


# USING BOOLENS 
"""
the "and" gives true only when all is true
the "OR" gives true if one of the value is true
the "NOT" gives true if the comparison turns out true
  it turns true to false and vice versa
"""

user = "admin"
logged_in = True

# and
if user == "admin" and logged_in:
    print("Admin page")
else:
    print("bad credentials"),


users = "admin"
logged_init = True

# or 
if users == "admin" or logged_init:
    print("Admin page")
else:
    print("bad credentials")



user = "admin"
logged_in = False

# not
if not logged_in:
    print("please log in")
else:
    print("welcome")