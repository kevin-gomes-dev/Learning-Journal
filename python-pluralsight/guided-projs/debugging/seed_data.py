import json

items_data = [
    {"item_id": 1, "item_name": "First Item", "A": 100, "B": 200, "D": 600, "E": 450},
    {"item_id": 2, "item_name": "Second Item", "A": 120, "B": 150, "D": 300, "E": 500},
    {"item_id": 3, "item_name": "Third Item", "A": 90, "B": 180, "D": 700, "E": 700}
]

bad_items_data = [
    {"item_id": 1, "item_name": "item missing key", "A": 100, "B": 200, "D": 600}, 
    {"item_id": 2,"item_name": "1st valid item","A": 200,"B": 400,"D": 300,"E": 600, "expected_value": 36120},  
    {"item_id": 3,"item_name": "item with invalid value type","A": "one hundred","B": 300,"D": 700,"E": 900},  
    {"item_id": 4, "item_name": "2nd valid item", "A": 100, "B": 200, "D": 500, "E": 300, "expected_value": 12090}, 
    {"item_id": 5}
]

# Write this data to a JSON file
base_file_path = 'data/items.json'

bad_item_file_path = 'data/bad_items.json'

with open(base_file_path, 'w') as json_file:
    json.dump(items_data, json_file, indent=4)

with open(bad_item_file_path, 'w') as json_file:
    json.dump(bad_items_data, json_file, indent=4)