import json
from typing import Any, Dict, List

# Doesn't make sense for the file path to be here as these are util funcs, should be modular
def load_item_data(fn):
    """Load item data from a JSON file."""
    try:
        with open(fn, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: JSON file not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return []


def calculate_item_value(A, B, D, E):
    """
    Calculate the dynamic price using the given formula:
    ((A + B) / 2) * (C * X + (1 - C))
    X and C depend on the relationship between D and E.
    """
    
    if D < E:
        X = A
        C = (E - D) / 500
    else:
        X = B
        C = (D - E) / 500

    return ((A + B) / 2) * (C * X + (1 - C))

def add_new_item(fn,item_list: List[Dict[str, Any]]):
    """Allow user to add a new item interactively."""

    item_name = input("Enter the item name: ")
    try:
        A = float(input("Enter value for A: "))
        B = float(input("Enter value for B: "))
        D = float(input("Enter value for D: "))
        E = float(input("Enter value for E: "))
        item_id = max([p["item_id"] for p in item_list], default=0) + 1
    except ValueError as e:
        print(str(e))
        return

    new_item = {
        "item_id": item_id,
        "item_name": item_name,
        "A": A,
        "B": B,
        "D": D,
        "E": E,
    }

    item_list.append(new_item)

    with open(fn, 'w') as file:
            json.dump(item_list, file, indent=4)

    print(f"item '{item_name}' added successfully!")


def validateItem(item: Dict[str, Any]):
    required_keys = ["item_id", "item_name", "A", "B", "D", "E"]
    for key in required_keys:
        # Validate key existence
        if key not in item:
            print(f'Item {item} not valid. Key missing: {key}')
            return False
        # Validate value type
        if key == "A" or key == "B" or key == "D" or key == "E":
            if not isinstance(item[key],(int,float)):
                print(f'Item {item} at key {key} is not an integer/float.')
                return False
    return True
