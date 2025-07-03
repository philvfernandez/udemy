class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

class WorkingStudent:
    def __init__(self, name, school, salary):
        self.name = name
        self.school = school
        self.marks = []
        self.salary = salary

    def average(self):
        return sum(self.marks) / len(self.marks)


phil = WorkingStudent('Phil', 'MIT', 15.50)
print(phil.salary)