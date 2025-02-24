from operator import truediv

age = 25

# result = age > 18 and age < 65 # True and True
# print(result)

result = age < 18 or age < 65  #false or true
print(result)


bool(0) # False, or zero
bool(13) # True

bool("") # False or empty screen
bool("Hello") # True

bool([]) # False or empty list
bool([1, 3, 5]) # True

default_age = 30
age = 0

user_age = age or default_age
print(user_age)

default_greeting = "there"
name = input("Enter your name: (optional) ")
user_name = name or default_greeting
print(f"Hello, {user_name}!")

age = int(input("Enter your age: "))
side_job = True
print(age > 18)
print(age > 18 and age < 65 or side_job) # or --> It returns the value after the or, if the value before the or evaluates to false.  So this statement evals to true.