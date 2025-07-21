import json

file = open('friends.json', 'r')
file_contents = json.load(file) #loads entire file and turns it into a dictionary.
file.close()

print(file_contents['friends'][0])

#write json to a file
cars = [
    {'make': 'Ford', 'model': 'Mustang'},
    {'make': 'Toyota', 'model': 'Rav4'}
]

file = open('cars.json', 'w')
json.dump(cars, file)
file.close()

my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'
incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])