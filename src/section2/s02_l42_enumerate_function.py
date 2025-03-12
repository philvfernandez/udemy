friends = ["Rolf", "John", "Anna"]
index = 0

# for friend in friends:
#    print(index)
#    print(friend)
#    index = index + 1

for index, friend in enumerate(friends):
    print(index)
    print(friend)

print(list(enumerate(friends)))

# Same as printing list of enumerate above
print(list(zip([0, 1, 2], friends)))

# Using a dict
print(dict(zip([0, 1, 2], friends)))

# Starting at index = 1
for index, friend in enumerate(friends, start=1):
    print(index)
    print(friend)
