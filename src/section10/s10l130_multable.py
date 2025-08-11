# Mutable - Something that can be changed after it's created.
# Immutable - Something that can't be changed after ti's created.
friends_last_seen = {
    'Rolf': 31,
    'John': 1,
    'Jack': 7,
}

# These are the same dictionary.
# another_variable = friends_last_seen

#How do you know something is mutable? It, the data, only lasts as long as it's in RAM and the program is running.

# This prints the memory address/id of the dictionary in memory.
print(id(friends_last_seen))

# This is a totally new dictionary in memory and will have a different id/address than the one above.
friends_last_seen = {
    'Rolf': 31,
    'John': 1,
    'Jack': 7,
}
print(id(friends_last_seen))

friends_last_seen['Rolf'] = 0 # friends_last_seen.__setitem__(self, 'Rolf')
#modifies the object above so the memory address/id will be the same because it's been
# changed or mutated.
print(id(friends_last_seen))

# Objects that are immutable: ints, floats, strings and tuples.  For example,
my_int = 5
print(id(my_int))

# This will print a totally different id/address in memory as the original int above that is set to 5.
my_int = my_int + 1 # my_int.__add__(self, 1): return cls(self.value + 1)
print(id(my_int))

my_int += 1 # my_int.__iadd__(self,1) --> creates a new int object every time. --> the new object is NOT mutable and can't be changed.

#List along with dictionaries are mutable.  For example: These two id's will have the same address.
friends_list = ['Rolf', 'John', 'Jack']
print(id(friends_list))
friends_list.append('Jill')
print(id(friends_list))
