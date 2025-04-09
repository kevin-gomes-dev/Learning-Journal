from __future__ import annotations
class Recipe:
  
  # Quicker data access, tuple non-mutable, no __dict__
  __slots__ = ('_name','_ingredients','_instructions')
  def __init__(self,name: str = "NULL",ingredients: list[dict] = [{"name":"NULL","quantity":"NULL"}],instructions: list[str] = ["NULL"]):
    self.name = name
    self.ingredients = ingredients
    self.instructions = instructions

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self,name):
    self._name = name

  @property
  def ingredients(self):
    return self._ingredients

  @ingredients.setter
  def ingredients(self,ind):
    self._ingredients = ind
    
  @property
  def instructions(self):
    return self._instructions

  @instructions.setter
  def instructions(self,ins):
    self._instructions = ins
    
  # Helper to create recipe if you don't want to manually type the structure
  @staticmethod
  def create_recipe() -> Recipe:
    r = Recipe()
    name = input('Enter name of recipe: ')
    if not name or name == '':
      print('No name provided.')
      return Recipe()
    ingredients = []
    while True:
      ing = input('Enter a single ingredient in pair of "name","quantity" including measurement, separated by a comma. Enter empty line to stop:\n')
      if not ing or ing == '':
        break
      ing_pair = ing.split(',')
      if len(ing_pair) < 2:
        print(f"Error: Couldn't parse ingredient you entered: {ing}. Please try again.")
      else:
        ingredients.append({"name": ing_pair[0],"quantity": ing_pair[1]})

    instructions = []
    while True:
      ins = input('Enter a single instruction which will be added in the order you enter. Enter blank line to exit:\n')
      if not ins or ins == '':
        break
      instructions.append(ins.strip())
      
    if len(instructions) == 0:
      instructions = None
    if len(ingredients) == 0:
      ingredients = None
    return Recipe(name,ingredients,instructions)

  # What happens if you do print(recipe_obj)
  def __str__(self):
    ingredient_str = ""
    for i in self.ingredients:
      ingredient_str += f'Ingredient Name: {i["name"]}, Ingredient Quantity: {i["quantity"]}\n'
    instruction_str = ""
    for i in self.instructions:
      instruction_str += i + '\n'
    return f'Recipe: {self.name}\n{ingredient_str}{instruction_str}'

  # What if you do repr(obj), for example to create one from a string
  def __repr__(self):
    return f'Recipe({repr(self.name)},{repr(self.ingredients)},{repr(self.instructions)})'
