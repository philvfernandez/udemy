ages = [22, 35, 27, 21, 20]
guests = ["Rolf", "ruth", "Charlie", "Jen"]
friends = ["jose", "Bob", "Rolf", "Charlie", "michael"]

odds = [age for age in ages if age % 2 == 1]
print(odds)

friends_lower = set([f.lower() for f in friends])
guests_lower = set([g.lower() for g in guests])
print(friends_lower.intersection(guests_lower))

present_friends = [
    name.title() for name in guests if name.lower() not in friends_lower
]
print(present_friends)