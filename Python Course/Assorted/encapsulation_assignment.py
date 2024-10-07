class Protected:
    def __init__(self):
        self._protectedVar = 10 # Protected prefix with a single underscore.

obj = Protected() # Creates the object inhereted from the class.
obj._protectedVar = 20 # Can still be changed, just noted with underscore that it should not be called outside of here.
print(obj._protectedVar) # Prints the value.




class Protected:
    # Initialized function that sets '_privateVar' as a int value of 99.
    def __init__(self):
        self.__privateVar = 99
    # Function that prints the previous function in the shell.
    def getPrivate(self):
        print(self.__privateVar) # Set to private with the double underscore prefix.
    # A new function that gets 'self' & 'private' passed in.
    def setPrivate(self, private):
        self.__privateVar = private # Shorter variable call.

obj = Protected() # Creates the object inhereted from the class.
obj.getPrivate() # Returns the value of the item with the specified key.
obj.setPrivate(92) # Sets the private variable a new value, only because it was instructed to do so.
obj.getPrivate() # Returns the value of the item with the specified key.

