import psycopg


def main():
  with psycopg.connect("dbname=dvdrental user=uq8273") as conn:

      # Open a cursor to perform database operations
      with conn.cursor() as cur:

          # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
          # of several records, or even iterate on the cursor
          cur.execute("SELECT (first_name || ' ' || last_name) FROM customer")
          for record in cur:
              print(record[0])

          # Make the changes to the database persistent
          conn.commit()


if __name__ == "__main__":
    main()
