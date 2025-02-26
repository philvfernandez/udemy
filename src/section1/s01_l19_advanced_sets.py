art_friends_advanced = {"Rolf", "Anne", "Jen"}
science_friends_advanced = {"Jen", "Charlie"}

# Elements that are in art but not in science
art_but_not_science = art_friends_advanced.difference(science_friends_advanced)
science_but_not_art = science_friends_advanced.difference(art_friends_advanced)

print(art_but_not_science)
print(science_but_not_art)

#Symmetric difference --> Those that are not in both sets
not_in_both = art_friends_advanced.symmetric_difference(science_friends_advanced)
print(not_in_both)

#Inserection --> The elements that are in both sets
art_and_science = art_friends_advanced.intersection(science_friends_advanced)
print(art_and_science)

#Union --> All elements in both sets and without duplicates
all_friends = art_friends_advanced.union(science_friends_advanced)
print(all_friends)