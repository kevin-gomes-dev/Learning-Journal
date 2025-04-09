from recipe import Recipe

# Makes more sense to have recipes in the cookbook, just like in real life
# Use static method in Recipe class to create recipes
recipes: list[Recipe] = []

# Given a raw dictionary, return Recipe
# Expects name, ingredients and instructions keys, creates a null Recipe otherwise
def make_recipe(raw_dict: dict) -> Recipe:
    try:
        return Recipe(raw_dict['name'],raw_dict['ingredients'],raw_dict['instructions'])
    except KeyError as e:
        print("Error: one of the keys in the dictionary given did not abide by Recipe standards. Dict given:",raw_dict)
        return Recipe()

# For quick testing for the demo
r = {
        "name": "Scrambled Eggs",
        "ingredients": [
            {"name": "eggs", "quantity": "3"},
            {"name": "milk", "quantity": "1/4 cup"},
            {"name": "salt", "quantity": "1/2 tsp"}
        ],
        "instructions": [
            "Beat eggs.", 
            "Add milk and salt.", 
            "Cook on low heat."
        ]
    }
recipes.append(make_recipe(r))

r = {
        "name": "Pancakes",
        "ingredients": [
            {"name": "eggs", "quantity": "2"},
            {"name": "milk", "quantity": "1/2 cup"},
            {"name": "flour", "quantity": "1 cup"},
        ],
        "instructions": [
            "Mix all ingredients.", 
            "Pour batter into pan.", 
            "Cook until golden brown."
        ]
    }
recipes.append(make_recipe(r))

def print_recipes(r_list: list[Recipe] = []):
    # We use str(x) to get string rep for list of recipes, printing each via its __str__ method
    # If we got a list in args, just print all of them
    print("\n".join([str(i) for i in r_list]))
  
def find_recipe_by_name(query_name) -> list[Recipe]:
    found_recipes = [recipe for recipe in recipes if query_name.lower() in recipe.name.lower()]
    return found_recipes

def find_recipes_by_ingredients(available_ingredients) -> list[Recipe]:
    matching_recipes = []
    for recipe in recipes:
        recipe_ingredients = [ingredient["name"] for ingredient in recipe.ingredients]
        if all(ingredient in recipe_ingredients for ingredient in available_ingredients):
            matching_recipes.append(recipe)
    return matching_recipes

def query_recipies():
    query_name = input("Enter the name of the recipe you want to search for: ")
    found_recipes = find_recipe_by_name(query_name)
    if len(found_recipes) == 0:
        print(f'No matching recipes found with name: {query_name}.')
    else:
        print(f'Found {len(found_recipes)} matching recipe{"" if len(found_recipes) == 1 else "s"}:')
        print_recipes(found_recipes)

def query_ingredients():
    available_ingredients = input("Enter the ingredients you have (comma-separated): ").split(',')
    available_ingredients = [ingredient.strip() for ingredient in available_ingredients]
    matching_recipes = find_recipes_by_ingredients(available_ingredients)
    
    if matching_recipes:
        print(f'You can make the following recipe{"" if len(matching_recipes) == 1 else "s"}:')
        print_recipes(matching_recipes)
    else:
        print("No recipes found with the given ingredients.")
    
def main():
    print("Welcome to the Recipe Book CLI Application!")
    
    while True:
        print("\nChoose an option:")
        print("1. List recipes")
        print("2. Query recipes")
        print("3. Search by ingredients")
        print("4. Add recipe")
        print("5. Exit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            print_recipes(recipes)
        elif choice == "2":
            query_recipies()
        elif choice == "3":
            query_ingredients()
        elif choice == "4":
            recipes.append(Recipe.create_recipe())
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break       
        else:
            print(f'Invalid choice: {choice}')

if __name__ == "__main__":
    main()