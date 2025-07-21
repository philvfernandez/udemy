file = open('csv_data.txt', 'r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]] # slicing a list that stores all lines in file other than the first line, which is the header.

for line in lines:
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].upper()
    degree = person_data[3].capitalize()

    print(f'{name} is {age}, studying {degree}, at {university}')

sample_csv_value = ','.join(['Rolf', '25', 'MIT', 'Computer Science'])
print(sample_csv_value)