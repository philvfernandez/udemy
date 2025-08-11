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