# This any() method takes an iterable and returns true if any of its elements evaluate to true.
# The and_all() method returns true if all of its elements evaluate to true
# List of dictionaries.
friends = [
    {
        'name': 'Rolf',
        'location': 'Washington D.C',
    },
    {
        'name': 'Jack',
        'location': 'San Francisco',
    },
    {
        'name': 'Jill',
        'location': 'San Francisco',
    },
    {
        'name': 'Jose',
        'location': 'San Francisco',
    },
]

your_location = input('Where are you right now? ')
friends_nearby = [friend for friend in friends if friend['location'] == your_location]

# another way to do above but we don't care about the length.
#if(len(friends_nearby) > 0):
  #  print('You are not alone!')

#so we can use the any() method
if(any(friends_nearby)):  # if truthy --> ones that evaluate to true; true if there's at least one;
                                                    # or False if they are empty
    print('You are not alone!')

if(all(friends_nearby)): print('You are alone!')    # If one is true then they all are true; T

"""
* 0, 0.0
* None
* [], (), {}
* False
"""

#Example
print(bool(0))
b = -0.0
# returns false because all non-zero numerical values evaluate to True, otherwise False.
# -0.0 is the same as 0, so it would evaluate to False.
print(bool(b))

b2 = 0.00000000000000000000001
# All non-zero numerical values evaluate to True, otherwise False.
print(bool(b2))

b3 = []
# Lists, sets and dictionaries all evaluate to False if they are empty, otherwise True.
print(bool(b3))

b4 = [None]
# Evaluates to True.  b is a list, and it only cares if it contains anything in itself when evaluating.
# Even if it just contains a None, by itself is not empty anymore, thus it evaluates to True.
print(bool(b4))

"""
Additional notes from quick and lectures:
The previous quiz asked you a few questions about whether certain numbers or objects evaluate to True  or False . It's not really something you have to know by heart, but over time you'll just know whether something evaluates to True  or False .

By the way, when we say "evaluates to True or False" we really mean this:

my_list = []
bool(my_list)  # False
 
another_list = [None]
bool(another_list)  # True
Your classes in Python can implement a magic method, __bool__ , which will tell bool() , if statements, and the sort, whether your object should evaluate to True  or False .

If you don't implement __bool__ , then __len__  will be used—if it returns 0  it will evaluate to False ; otherwise it will evaluate to True .

Finally, if you don't implement either __bool__  or __len__ , your object will always evaluate to True .

Learn more here: https://docs.python.org/3/library/stdtypes.html#truth-value-testing
"""