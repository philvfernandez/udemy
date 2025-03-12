friends = ["jose", "Bob", "Rolf", "Charlie", "michael"]
guests = ["Rolf", "ruth", "Charlie", "Jen"]


friends_lower = {n.lower() for n in friends}
guests_lower = {n.lower() for n in guests}

present_friends = friends_lower.intersection(guests_lower)
present_friends = {name.title() for name in present_friends}
print(present_friends)

friends2 = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = {
    friends2[i]: time_since_seen[i]
    for i in range(len(friends2))
    if time_since_seen[i] > 5
}
print(long_timers)

