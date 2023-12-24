import json
import os


def read_json(file_path: str) -> list:
    new_path = os.path.join(os.path.dirname(__file__), "..", f"data/{file_path}")
    with open(new_path, encoding="utf-8") as f:
        json_obj = json.load(f)
    return json_obj
