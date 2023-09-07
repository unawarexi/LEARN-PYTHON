print('imported my_module')

test = 'Test_string'

def find_index(to_search, target):
    '''finds the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1


"""
1.Built-in Functions: These are functions that are available without the need for an explicit import.

2.Built-in Types: Modules related to fundamental data types.
datetime: Date and time handling.
math: Mathematical functions.
random: Random number generation.
collections: Data structures like lists, dictionaries, etc.
itertools: Tools for working with iterators and combinatorial functions.

3.File and Directory Access: Modules for file and directory manipulation.
os: Operating system interface.
shutil: High-level file operations.
pathlib: Object-oriented filesystem paths


4.Data Persistence and Serialization:
pickle: Serialization and deserialization of Python objects.
json: JSON encoding and decoding.
sqlite3: SQLite database access.


5.Networking and Internet:
socket: Low-level networking.
http: HTTP client and server libraries.
urllib: URL handling and HTTP client functions.


6.GUI Programming:
tkinter: Standard GUI library for Python.
turtle: Turtle graphics for educational purposes.


7.Multithreading and Multiprocessing:
threading: Thread-based parallelism.
multiprocessing: Process-based parallelism.


8.Debugging and Profiling:
pdb: The Python Debugger.
cProfile: Performance analysis.


9.Regular Expressions:
re: Regular expression operations.

10.Command Line Arguments and Environment:
argparse: Command-line parsing.
os.environ: Environment variables.

11.Unit Testing:
unittest: Unit testing framework.
doctest: Testing through interactive documentation.

12.Utilities:
sys: System-specific parameters and functions.
time: Time-related functions.
subprocess: Subprocess management.
logging: Logging facility.

13.Data Compression and Archiving:
zipfile: Work with ZIP archives.
gzip, bz2: Compression formats.

14.Internationalization and Localization:
locale: Internationalization support.
gettext: Multilingual internationalization.

15.Security:
hashlib: Hash functions.
ssl: SSL/TLS support.
This is just a small subset of the Python Standard Library modules and their functions. Each module provides a range of classes and functions tailored to specific tasks. To learn more about a particular module and its functions, you can refer to the official Python documentation: https://docs.python.org/3/library/
"""