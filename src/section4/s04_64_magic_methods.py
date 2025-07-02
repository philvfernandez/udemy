from src.section2.s02_l29_for_loops import index


class Student:
    def __init__(self, name):
        self.name = name

## Special Python Methods
movies = ['Matrix', 'Finding Nemo']

## Returns class list.  So that means the movies list is an object.  As everything in Python is an object
print(movies.__class__)

## Returns a string (str) class
print("hi".__class__)

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

    ## returns a string that represents an object.
    # If you are only going to implement one of these, you should implement only the __repr__ method
    def __repr__(self):
        return f'<Garage {self.cars}>'

    def __str__(self):
        return f'Garage with {len(self.cars)} cars.'


ford = Garage()
print(ford.cars)
ford.cars.append('Fiesta')
ford.cars.append('Focus')
print(ford.cars)
print(len(ford))
print(ford[0]) ## Same as Garage.__getitem__(ford, 0

## Note from course.... You only need __getitem__ and not __len__, to be able to for-loop over an object
for car in ford:
    print(car)

print(ford)