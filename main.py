import psycopg

def main():
  with psycopg.connect("dbname=kitchen_sink user=uq8273") as conn:

      # Open a cursor to perform database operations
      with conn.cursor() as cur:

          # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
          # of several records, or even iterate on the cursor
          cur.execute("SELECT (recipes).ingredients FROM recipe_col")
          for record in cur:
              print(record[0][0])

          # Make the changes to the database persistent
          conn.commit()


if __name__ == "__main__":
    main()
