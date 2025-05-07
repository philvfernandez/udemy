def add(x,y=3):  #example of a default parameter
    total = x + y
    return total

print(add(5,10))
print(add(x=3))
print(add(x=5, y=2))  # example of named arguments

## This will cause an error because there is no name given for the second named parameter.
# print(add(x=5, 2))

#example of separate
print(1, 2, 3, 4, 5, sep=" - ")

#default values
default_y = 3
def add(x, y=default_y):
    total = x + y
    print(total)

add(2)

#The result of this will still be five because the original value of default_y is used.
default_y = 4
add(2)