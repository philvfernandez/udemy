get_input = True
while get_input:
    user_input = input("Type either p or q. ")
    if user_input == 'p':
        print("Hello")
    get_input = user_input != 'q'
