friends = ["Rolf", "Bob", "Anne"]
#print(friends[0])
#print(friends[1])
#print(len(friends))

friends_ages = [
    ["Rolf", 24], ["Bob", 30], ["Anne", 27]
]

print(friends_ages[0][0])
print(friends_ages[1][1])

# This would be more readable
friends_multi = [
    ["Rolf", 24],
    ["Bob", 30],
    ["Anne", 27],
    ["Charlie", 25],
    ["Jen", 25],
    ["Adam", 29],
]

friends.append("Jen");
print(friends)
friends.remove("Jen");
print(friends)

friends_multi.remove(["Anne", 27]);
print(friends_multi)