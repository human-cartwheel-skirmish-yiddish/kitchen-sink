class Recipe:
  __slots__ = ["category", "name", "ingredients", "steps"]

  def __init__(self, category, name, ingredients, steps):
    self.category = category
    self.name = name 
    self.ingredients = ingredients 
    self.steps = steps

def parse_recipes(filename):
  recipes = []
  with open(filename) as f:
    for line in f:
      items = line.split(";");
      recipes.append(Recipe(items[0], items[1], items[2].split("|"), items[3].split("|")))

  return recipes
    