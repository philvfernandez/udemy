numbers = [0, 1, 2, 3, 4]
doubled_numbers = []

for number in numbers:
    doubled_numbers.append(number*2)

print(doubled_numbers)

#Using a list comprehension to double numbers in a list
doubled_numbers = [number*2 for number in numbers]
print(doubled_numbers)

## Using range instead of a list
doubled_numbers = [number*2 for number in range(5)]
print(doubled_numbers)

friends_ages = [22, 31, 35, 37]
age_strings = [f"My friend's age is {age} years old" for age in friends_ages]
print(age_strings)

## Transform strings in array to all lower case strings
names = ["Ralf", "Bob", "Jen"]
lower = [name.lower() for name in names]
print(lower)

friend = input("Enter a friend's name: ")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friends_lower = [name.lower() for name in friends]
if friend.lower() in friends_lower:
    print(f"{friend.title()} is one of your friends")