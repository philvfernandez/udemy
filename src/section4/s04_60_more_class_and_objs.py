## Dictionary
my_student = {
    'name' : 'Phil Fernandez',
    'grades' : [70, 88, 90, 99],
    'average' : None ## something that calculates average
}

def calculate_grades(my_student):
    return sum(my_student['grades']) / len(my_student['grades'])

# print(calculate_grades(my_student))

## There is a flaw in the software design of the above.  The flaw is the two functions calculate_grades and sum
## are not related and are disjointed.  Basically they are tightly coupled.  Meaning the average_grade function
## requires a student dictionary and a grades index into the dictionary.  This would cause issues if the function
## was in a totally different file or location than the dictionary.  For example, if you changed 'grades' in the
## dictionary to 'results', it would break what's referenced in the average_grade function.

## If we added an average to the dictionary, it would need to be a function that calculates the average and still
## be part of the dictionary.  However, that is not possible.  So we will need to have classes and objects.

## An object stores data and actions that operate on that data.

## The functions inside a class that start with '__' are called doneder functions. THey are special python functions.

class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def print_info(self):
        print(f"<<{self.name}>> grades {self.grades}")


## Creates an object of type Student
student_one = Student('Tawnee Fernandez', [70, 88 ,90, 99])
student_two = Student('Jose', [50, 68, 99, 100])

## print(student_one.name)
## print(student_two.name)

## Prints the type of the class which in this case is of type Student
## print(student_one.__class__)

print(student_one.average())

## What happens in the background when you call print(student_one.average())
print(Student.average(student_one))

print(student_one.grades)
def average(student):
    return sum(student.grades) / len(student.grades)
print(average(student_one))

student_one.print_info()

