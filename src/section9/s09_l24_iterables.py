# An iterable is an object that has an iter method.
# def __iter__(self): # Object becomes an iterable

## Remember....
## Iterator: used to get the next value
## Iterable: used to go over all the values of the iterator

class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return self # self is the iterator object


##class FirstHundredIterable:
##    def __iter__(self):
 ##       return FirstHundredGenerator()

print(sum(FirstHundredGenerator()))

for i in FirstHundredGenerator():
    print(i)

class AnotherIterable:
    def __init__(self):
        self.cars = ['Fiesta', 'Focus']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]


for car in AnotherIterable():
    print(car)

my_numbers = [x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]] ## list compression
my_numbers_gen = (x for x in [1,2,3,4,5,6,7,8,9])  # now a generator --> short hand for iterating over a list.
print(next(my_numbers_gen))