friends = ['Ralf', 'Jen', 'Anne']

for friend in friends:
    print(friend)

elements = [0,1,2,3,4,5,6,7,8,9]
for element in elements:
    print(element)

for _ in elements: ## Using the '_' when we don't want to use a variable in the for loop
    print("hello world!")

for index in range(10): ## Still print 10 times w/o having to use the list variable
    print(index)

for index in range(5, 10): ## Prints numbers from 5 to 10
    print(index)

for index in range(2, 20, 3): ## prints numbers from 2 to 19 with only every three numbers printed
    print(index)

students = [
    {"name": "Ralf", "grade": 90},
    {"name": "Bob", "grade": 78},
    {"name": "Jen", "grade": 100},
    {"name": "Anne", "grade": 80},
]

for student in students:
    name = student["name"]
    grade = student["grade"]
    print(f"{name} grade is {grade}")