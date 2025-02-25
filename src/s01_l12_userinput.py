my_name = "Jose"
your_name = input("Enter your name: ")

print(f"Hello, {your_name}!  My name is {my_name}.")

age = input("Enter your age: ")
age_num = int(age)
print(f"You have lived for {age_num * 12} months.")

## You can also do a tested call that gets the input and converts it to an int.
age = int(input("Enter your age: "))
print(f"You have lived for {age * 12} months.")

## Coding exercise
##Part 1
your_name = input("Enter your name: ").upper()
print(f"Hello, {your_name}.")

age = int(input("Enter your age: "))
print(f"You have lived for {age * 12} months.")
