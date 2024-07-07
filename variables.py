"""
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
"""
x = 5             # x is of type int
y = "John"        # x is now of type str
print(x)
print(y)
print(type(x))    # by using this statment we can verify the type of any variable.
print(type(y))

a = str(3)    # x will be '3'
b = int(3)    # y will be 3
c = float(3)  # z will be 3.0
print(a)       
print(b)
print(c)

# Variable names are case-sensitive.
d = 4
D = "Sally"          #A will not overwrite a
print(d)
print(D)