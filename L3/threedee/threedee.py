import json

file = "./rabbit_challenge.json"

with open(file) as f:
    data = json.load(f)


data_processed = {
    'vertices': [],
    'edges': []
}

keys = data.keys()

print(keys)

for key in keys:
    for value in data[key]:
        if value.get('color') == '#0b0f14':
            _value = value
            _value['color'] = '#ffffff'
            data_processed[key].append(_value)

with open('data_processed.json', 'w') as f:
    json.dump(data_processed, f, indent=4)
