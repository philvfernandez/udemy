def interact():
    while True: # keep looping until user reaches break statement
        try:
            user_input = int(input("Please input an integer: "))
        except ValueError:
            print("Please input integers only.")
        else:
            # print out the message '{user_input} is {even/odd}.
            print('{} is {}.'.format(user_input, 'even' if user_input % 2 == 0 else 'odd'))
        finally:
            user_input = input('Do you want to play again? (y/n): ')
            if(user_input != 'y'): # quit if the user didn't input 'y'
                print('Goodbye!')
                break
interact()