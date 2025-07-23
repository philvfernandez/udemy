import json

# file = open('friends.json', 'r')
#file_contents = json.load(file) #loads entire file and turns it into a dictionary.
# file.close()

# Using with syntax.  Note: This automatically closes the file for us.
with open('friends.json', 'r') as file: # Also known as a context manager.
    file_contents = json.load(file)  # loads entire file and turns it into a dictionary.



print(file_contents['friends'][0])

#write json to a file
cars = [
    {'make': 'Ford', 'model': 'Mustang'},
    {'make': 'Toyota', 'model': 'Rav4'}
]

with open('cars.json', 'w') as file:
    json.dump(cars, file)

my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'
incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])