""" 
1. classes are generic  and not specific 
2. they contain the objects
3. 

"""

# Note: attributes and methods can change depending on the object requirements

class car:
    # these are attributes()
    # __init__ is a dunder or magic function
    
    def __init__(self, name, brand, year, model):
        self.name = name
        self.brand= brand
        self.year = year
        self.model = model
    
    # this is a method (functions)
    def auto() :
        pass
    
# this is an instance or object 
car1 = car("corrolla", "toyota", "2022", "2vgx")