"""
* counter
* defaultdict
* ordereddict
* namedtuple
* deque
"""

from collections import Counter

#counter example
device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0,  16.0]

temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.0])

Counter({'hello': 5, 'hi': 6})
print(Counter({'hello': 5, 'hi': 3})['hi'])

#defaultdict example
from collections import defaultdict
coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]

alam_masters = {}
for coworker in coworkers:
    if coworker[0] not in alam_masters:
        alam_masters[coworker[0]] = []
    alam_masters[coworker[0]].append(coworker[1])

alam_masters_2 = defaultdict(list) # defaultdict takes in a default method --> list() --> which returns an empty list
for coworker, place in coworkers:
    alam_masters_2[coworker].append(place)

# alam_masters_2.default_factory = None # Will force an error of key does not exist.  Example below for key 'Anne'
print(alam_masters_2['Rolf'])
print(alam_masters_2['Anne'])

my_company = 'Teclado'
coworkers2 = ['Jen', 'Li', 'Charlie', 'Rhys']
other_coworkers = [('Rolf', 'Apple Inc.'), ('Jen', 'Google')]
coworker_companies = defaultdict(lambda: my_company )
for person, company in other_coworkers:
    coworker_companies[person] = company

print(coworker_companies[coworkers2[0]])
print(coworker_companies[coworkers2[0][0]])

#ordereddict example
from collections import OrderedDict
o = OrderedDict()
o['Rolf'] = 6
o['Jose'] = 12
o['Jen'] = 3

# Note: regular dictionaries will all be ordered as of python 3.7
print(o)
o.move_to_end('Rolf')
o.move_to_end('Jen', last=False)
print(o)
o.popitem()
print(o)

#namedtuple - Useful for when you want to read from a file or a database.
from collections import namedtuple
account = ('checking', 1850.90)
print(account[0]) # this does not really tell us what account[0] is.  So you should use a namedtuple
print(account[1])

Account = namedtuple('Account', ('name', 'balance'))
account = Account('checking', 1850.90)
print(account.name)
print(account.balance)

accountNamedTuple = Account._make(account) # takes in a tuple.  Useful if you want to use the map function
print(accountNamedTuple._asdict())

# Deque --> Double ended queue.  Note deque thread safe
from collections import deque
friends = deque(('Rolf', 'Jen'))
friends.append('Jose') #appends to the end of queue
friends.appendleft('Anthony') # appends to the left of queue
friends.pop() # Removes element from the end
friends.popleft() # Removes element from the start