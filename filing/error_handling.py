# # Error Handling: in python are simply ways to catch errors in python programming.
"""
SYNTAX:
try:
    block_of_code...
except:
    block_of_code...
finally:
    block_of_code...
"""

# print("Before Execution")
# print(2/0)
# print("After Execution")

# print("Before Execution")
# try:
#     print('\t', 2/0)
# except ZeroDivisionError as error:
#     print(f"ERROR: {error}")
# except:
#     print("something happened!!!")

# print("After Execution")

a = 5
b = 6

try:
    c = a + d
    print('\t', c)
except NameError as error: # Error 1
    print('ERROR: ', error)
finally:
    print('I handled that error like a pro!!!')