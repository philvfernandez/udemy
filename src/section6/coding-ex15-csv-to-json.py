import json

# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:
#The according keys to each field in the CSV file are club, city and country. Thus the output should be, according to the given sample CSV file, like this:

#[{"club": "Manchester United", "country": "UK", "city": "Manchester"}, {"club": "Real Madrid", "country": "Spain", "city": "Madrid"},
# {"club": "Juventus", "country": "Italy", "city": "Turin"}]

csv_file = open('csv_file.txt', 'r')
json_file = open('json_file.txt', 'w')

# custom keys for json file
custom_keys = ['club','city','country']
data = []

for line in csv_file.readlines():
    values = line.strip().split(',')

    # Pair custom keys with values
    row_dict = dict(zip(custom_keys, values))
    data.append(row_dict)


json.dump(data, json_file)
csv_file.close()
json_file.close()


