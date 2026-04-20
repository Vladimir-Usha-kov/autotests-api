import json

data = {"name": "vova", "age": 27}


with open('names.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

