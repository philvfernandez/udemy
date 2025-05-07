# Lamda functions are used to get inputs, do some processing and return an output

#Go example of a function that can be used as a lamda function instead.
#def divide(x, y):
 #   return x / y

# Example of a lamda function
divide = lambda x, y: x / y

#You can call the lamda like any other function
print(divide(1, 2))

#Python will just destroy this lamda function because it's not being used.
lambda x, y: x / y

#Another way to use the Lamda function but nothing will get printed out.  Not really encouraged.
(lambda x, y: x / y)(15,3)

# Messy so don't do this because it's not very readable with all the brackets
print((lambda x, y: x / y)(15,3))


def average(sequence):
    return sum(sequence) / len(sequence)

students = [
    {"name": "Rolf", "grades": (60, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    print(average(student["grades"]))

# The above average function refactored to use a lamda function
average = lambda sequence: sum(sequence) / len(sequence)