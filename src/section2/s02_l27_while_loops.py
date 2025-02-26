is_learning = True
while is_learning:
    print("You're Learning")
    # is_learning = False ## breaks from loop
    user_input = input("Are you still Learning?")
    is_learning = user_input == "yes"

print("Bye...")