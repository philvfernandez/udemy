# IndexError --> Index out of range exception is thrown.
# KeyError --> Non-existing key given.
# NameError --> The variable is not defined.
# AttributeError --> The object does not have the given attribute.
# NotImplementedError --> Example listed below
# RuntTimeError --> Happens when you run your program.  Base error that's not thrown by python a lot.
# SyntaxError --> A code based error within the syntax of the given code.
# indentationError --> A syntax based error related to an incorrect indentation error.
# TabError --> This error is thrown if you are mixing and matching indentation like tabs and spaces.
# TypeError --> assigning one type to another type.  Both types should be the same.
# ValueError --> Happens when you give built-in functions a value of the correct type but incorrect value.
# For example: When using a string inside an int() method call. --> int('20.5')
# ImportError --> happens when you get a circular import.  One file imports another which then imports the first file.
# DeprecationWarning --> A warning and not an error.  Deprecated means it's not longer the best way of doing something.
## Or a python based code that's no longer used or is the current code base to use.

# But....
# - Often you won't be raising any of these exceptions.
# - *** You should create your own exceptions, with even better names!


# A NontImplementedError with the raised given error will be thrown if this code is executed.
#class User:
#    def __init__(self, username, password):
#        self.username = username
#        self.password = password

#   def login(self):
#        raise NotImplementedError('This feature has not been implemented yet.')

# Example of an indentation error
#def add_two(x, y):
#return x + y