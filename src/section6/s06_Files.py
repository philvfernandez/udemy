my_file = open('/mnt/c/Edit/Dev/udemy/complete-python-course/src/section6/data.txt', 'r')
file_content = my_file.read()

my_file.close()
print(file_content)

user_name = input('Enter your name: ')
my_file_writing = open('/mnt/c/Edit/Dev/udemy/complete-python-course/src/section6/data.txt', 'w') ## Erases any data currently in the file.
my_file_writing.write(user_name)
my_file_writing.close()
