class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

phil = Student('Phil', 'MIT')

phil.marks.append(78)
phil.marks.append(99)

# This is called an instance method which takes an object as the first argument.
print(phil.average())


class Foo:
    @classmethod
    ## This is a class method that uses cls to hold the value of the class that it was called with.
    ## So in this case it's Foo
    def hi(cls):
        print(cls.__name__)

my_object = Foo()
## The objects class is being passed as the first argument to the hi method.
my_object.hi()

## Example of using a static method
class Bar:
    @staticmethod
    def hi():
        print('Hello, I do no take parameters.')

another_object = Bar()
another_object.hi()