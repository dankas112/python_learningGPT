import json

users = [
    {"id": 1, "name": "Max"},
    {"id": 2, "name": "Danya"},
    {"id": 3, "name": "Ilya"}
]

try:
    with open('users_lib.json', 'w', encoding='utf8') as f:
        json.dump(users, f, ensure_ascii=False, indent=4)
    
    with open('users_lib.json', 'r', encoding='utf8') as f:
        text = json.load(f)
        print(text)
        for user in text:
            print(f"id: {user['id']}, name: {user['name']}")    
        
except FileNotFoundError:
    print('Файла не существует')
except json.JSONDecodeError:
    print('Файл поврежден')