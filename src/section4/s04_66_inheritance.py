class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

## WorkingStudent is a child of Student or it extends Student
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        ## Super is the parent class (Student)
       super().__init__(name, school)
       self.salary = salary

    def weeklySalary(self):
        return self.salary * 37.5



phil = WorkingStudent('Phil', 'MIT', 15.50)
print(phil.salary)
phil.marks.append(57)
phil.marks.append(99)
print(phil.average())
print(phil.weeklySalary())


## This will return an error because there is no weekly_salary defined in the Student class.  It's only defined
## in the Working_Student class.  Which is to say that WorkingStudent gets stuff from Student.  And not the other
## way around.
## anna = Student('Anna', 'Oxford')
## print(anna.weekly_salary())