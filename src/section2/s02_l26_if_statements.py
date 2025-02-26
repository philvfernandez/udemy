friend = "Ralf"
user_name = input("Enter your name: ")

if user_name == friend:
    print("Hello, friend!!")
    print("This Runs Too")
else:
    print("Names are not equal")


print(bool(5)) ## True
print(bool(0)) ## False

if 5:
    print("Runs")

name = input("Enter your name: ")
if name:
    print("We already know your name.")

friends = ["Ralf", "Bob", "Anne"]
family = ["Jen", "Charlie"]

user_name = input("Enter your name: ")

if user_name in friends:
    print("Hello, friend!!")
elif user_name in family:
    print("Hello, family!!")
else:
    print("I don't know your you.")
