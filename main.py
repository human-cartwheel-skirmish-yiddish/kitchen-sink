from thefuzz import fuzz
import query


def main():
    filename = "./recipes.txt"
    # query.insert_from_data(filename)
    query.show_recipes_name()

if __name__ == "__main__":
    main()
