## Dictionary
my_student = {
    'name' : 'Phil Fernandez',
    'grades' : [70, 88, 90, 99]
}

def calculate_grades(my_student):
    return sum(my_student['grades']) / len(my_student['grades'])

print(calculate_grades(my_student))

## There is a flaw in the software design of the above.  The flaw is the two functions calculate_grades and sum
## are not related and are disjointed.  Basically they are tightly coupled.  Meaning the average_grade function
## requires a student dictionary and a grades index into the dictionary.  This would cause issues if the function
## was in a totally different file or location than the dictionary.  For example, if you changed 'grades' in the
## dictionary to 'results', it would break what's referenced in the average_grade function.