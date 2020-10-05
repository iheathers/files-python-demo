import json

with open('friends_json', 'r') as file:
    file_content = json.load(file)  # reads file and turns it into dictionary

print(file_content)
print(type(file_content))

cars = [
    {'make': 'Tesla', 'model': 'Fiestaa'},
    {'make': 'Elon', 'model': 'Musk'}
]

with open('json_data.txt', 'w') as output_file:
    json.dump(cars, output_file, indent=4)
