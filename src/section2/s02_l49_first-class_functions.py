def greeting():
    print("Hello")

greeting()

# Functions Are First-class --> Assigning the variable the value that the function references.
hello = greeting
hello()

#Another example of using functions as a first-class citizens.
#def average(seq):
#    return sum(seq) / len(seq)

avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)  # This can be simplified to sum
top = lambda seq: max(seq)

operations = {
    "average": avg,
    "total": total,
    "top": top,
}

students = [
    {"name": "Rolf", "grades": (60, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student {name}")
    operation = input("Enter 'average', total', or 'top': ")

    ## Replaces the if and elif statements below
    operation_function = operations[operation]
    print(operation_function(grades))

'''
    if operation == "average":
        print(avg(grades))
    elif operation == "total":
        print(total(grades))
    elif operation == "top":
        print(top(grades))
'''

