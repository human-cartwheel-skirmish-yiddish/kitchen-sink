from thefuzz import fuzz
import query


def main():
    filename = "./recipes.txt"
    ingredients = query.get_recipes_ingredients()
    for ingredient in ingredients:
      print(ingredient)    

if __name__ == "__main__":
    main()
