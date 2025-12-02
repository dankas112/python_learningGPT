import json
try:
    with open("scores.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        print(data)
    data["score"] = 150

    with open("scores.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

except json.JSONDecodeError:
    print('Файл поврежден')
except FileNotFoundError:
    print('Файл отсутствует')