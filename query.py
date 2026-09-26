import psycopg
import recipe

def insert_from_data(filename):
  recipes = recipe.parse_recipes(filename)
  with psycopg.connect("dbname=kitchen_sink user=uq8273") as conn:
    with conn.cursor() as cur:
      for aRecipe in recipes:
        cur.execute("INSERT INTO recipe_col(recipes, user_id) VALUES(ROW(%s, %s, %s, %s), 1)", (aRecipe.category, aRecipe.name, aRecipe.ingredients, aRecipe.steps)) 

      conn.commit()

def show_recipes_name():
  with psycopg.connect("dbname=kitchen_sink user=uq8273") as conn:
    with conn.cursor() as cur:
      cur.execute("SELECT (recipes).name  FROM recipe_col")
      for record in cur:
        print(record[0])
      
def get_recipes_ingredients():
  ingredients = []
  with psycopg.connect("dbname=kitchen_sink user=uq8273") as conn:
    with conn.cursor() as cur:
      cur.execute("SELECT id, (recipes).ingredients FROM recipe_col")
      for ing in cur:
        ingredients.append((ing[0], ing[1]))
  
  return ingredients
        
def delete_recipes():
   with psycopg.connect("dbname=kitchen_sink user=uq8273") as conn:
    with conn.cursor() as cur:
      cur.execute("DELETE FROM recipe_col")
      conn.commit()
