import json
INPUT_FILE = "input.json"
def task() -> float:
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        json_data = json.load(f)
        total = 0
        for items in json_data:
            score = float(items.get("score"))
            weight = float(items.get("weight"))
            total += score * weight
    return round(total, 3)


print(task())
