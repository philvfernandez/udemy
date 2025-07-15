# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to the file 'nearby_friends.txt'
# hint: readlines()
from src.section1.s01_l16_lists import friends

# My solution
"""
my_file_writing = open('/mnt/c/Edit/Dev/udemy/complete-python-course/src/section6/nearby_friends.txt', 'a') ## Erases any data currently in the file.
for index in range(3):
user_input = input("Enter your 3 friends: ")
with open("/mnt/c/Edit/Dev/udemy/complete-python-course/src/section6/people.txt", "r") as file:
    for line in file:
        # print("user input is: ", user_input)
        if(user_input == line.strip()):
            print("user_input matches name in people.txt file")
            my_file_writing.write(line)
file.close()
my_file_writing.close()

# Solution from lecture
friends = input('Enter three friend names, separated by commas (no spaces please').split(',')
people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()] # [line1, line2, line3, line4]
people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)
friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open('nearby_friends.txt', 'w')
for friend in friends_nearby_set:
print(f'{friend} is nearby! Meet with them.')
nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()

"""
