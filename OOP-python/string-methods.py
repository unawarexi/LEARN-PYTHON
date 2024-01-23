"""
they are different kind of methods for each datatype
methods are functions belonging to an object

TYPES OF METHODS IN PYTHON
 - static methods
 - class methods
 - instance methods

"""

# STRING METHODS"""
# use print(dir) to know the methods available for usage
# use print(help(str.method)) to know what it does
# """
# FORMATTING & STRING CONCAT

#================= STRING METHODS ====================
#""" Python provides a wide range of string methods that you can use to manipulate and work with strings. Here's a list of some common string methods along with their descriptions:
"""
1. `str.capitalize()`: Converts the first character of a string to uppercase and the rest to lowercase.

2. `str.upper()`: Converts all characters in the string to uppercase.

3. `str.lower()`: Converts all characters in the string to lowercase.

4. `str.title()`: Converts the first character of each word in the string to uppercase and the rest to lowercase.

5. `str.swapcase()`: Converts uppercase characters to lowercase and vice versa.

6. `str.strip()`: Removes leading and trailing whitespace (or specified characters) from the string.

7. `str.lstrip()`: Removes leading whitespace (or specified characters) from the string.

8. `str.rstrip()`: Removes trailing whitespace (or specified characters) from the string.

9. `str.startswith(prefix)`: Returns `True` if the string starts with the specified prefix.

10. `str.endswith(suffix)`: Returns `True` if the string ends with the specified suffix.

11. `str.count(substring)`: Returns the number of non-overlapping occurrences of a substring in the string.

12. `str.find(substring)`: Returns the lowest index of the substring in the string, or -1 if not found.

13. `str.index(substring)`: Similar to `find()`, but raises a `ValueError` if the substring is not found.

14. `str.replace(old, new)`: Replaces occurrences of a substring with another substring.

15. `str.split(separator)`: Splits the string into a list of substrings based on the specified separator.

16. `str.join(iterable)`: Joins elements of an iterable (e.g., a list) into a single string using the string as a separator.

17. `str.isalnum()`: Returns `True` if all characters in the string are alphanumeric.

18. `str.isalpha()`: Returns `True` if all characters in the string are alphabetic.

19. `str.isdigit()`: Returns `True` if all characters in the string are digits.

20. `str.islower()`: Returns `True` if all characters in the string are lowercase.

21. `str.isupper()`: Returns `True` if all characters in the string are uppercase.

22. `str.isspace()`: Returns `True` if all characters in the string are whitespace.

23. `str.startswith(prefix)`: Returns `True` if the string starts with the specified prefix.

24. `str.endswith(suffix)`: Returns `True` if the string ends with the specified suffix.

25. `str.encode(encoding)`: Returns a bytes object encoding the string using the specified encoding.

26. `str.format()`: Formats the string using placeholders and substitutions.

27. `str.isnumeric()`: Returns `True` if all characters in the string are numeric.

28. `str.partition(separator)`: Splits the string into a 3-tuple based on the first occurrence of the separator.

29. `str.rpartition(separator)`: Splits the string into a 3-tuple based on the last occurrence of the separator.

30. `str.zfill(width)`: Pads the string with zeros to the specified width.
"""
# These are just some of the most commonly used string methods in Python. You can find more details and examples for each method in the official Python documentation: https://docs.python.org/3/library/stdtypes.html#string-methods




greetings = "hello"
name = "peter"

info = f"{greetings}, {name}. welcome!"
print(info.upper())
# using string methods
