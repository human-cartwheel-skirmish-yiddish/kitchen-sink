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
      cur.execute("SELECT (recipes).name FROM recipe_col")
      for record in cur:
        print(record[0])