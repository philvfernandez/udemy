#tuples
currencies = (8.8, 1.2)
## Get first value of tuple and store it in usd.  Then get the second and store it in eur
usd, eur = currencies

## A list of tuples
friends = [("Ralf", 25), ("Anne", 37), ("Charlie", 31), ("Rob", 22)]
for friend in friends:
    print(friend)

## Better way to loop through friends
for name, age in friends:
    print(name, age)
    ## Using an f string to format
    print(f"{name} is {age} years old")


