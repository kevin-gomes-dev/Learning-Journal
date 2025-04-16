import pdb
from typing import Any, Dict, List
import calc_util


def main():
    JSON_FILE_PATH = 'data/bad_items.json'
    items: List[Dict[str, Any]] = calc_util.load_item_data(JSON_FILE_PATH)
    if not items:
        print("No items found in the JSON file.")
        
    while True:
        print("\nItem Values:")
        for item in items:
        #   pdb.set_trace()
          if calc_util.validateItem(item):
            item_val = calc_util.calculate_item_value(
              item["A"], item["B"], item["D"], item["E"]
            )
            print(f"Item: '{item['item_name']}' Value: {item_val:.2f}")

        choice = input("\nWould you like to add a new item? (yes/no/exit): ").strip().lower()

        if choice == "yes":
            calc_util.add_new_item(JSON_FILE_PATH,items)

        elif choice == "no":
            print("No changes were made.")

        elif choice == "exit":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please type 'yes', 'no', or 'exit'.")


if __name__ == "__main__":
    main()
