CREATE TYPE Recipe AS (
  category varchar(100),
  name varchar(100),
  ingredients text[],
  steps text[]
);

CREATE TYPE Person AS (
  username varchar(100),
  password varchar(100)
);

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  details Person
);

CREATE TABLE recipe_col (
  id SERIAL PRIMARY KEY,
  recipes Recipe,
  user_id INT,
  FOREIGN KEY (user_id) REFERENCES users (id)
);

INSERT INTO users (details, user_id)
VALUES (
  ROW(
    'uq8273',
    'password'
  ),
  1
);

INSERT INTO recipe_col (recipes, user_id)
VALUES (
  ROW(
    'dinner',
    'Tomato and Eggs',
    ARRAY['Eggs', 'Garlic', 'Ginger', 'Green Onions', 'Tomato', 'Sugar'], 
    ARRAY['Mix egg with onions', 'Scramble eggs', 'Put aside', 'Cook tomatoes on ginger, garlic', 'Add water if needed', 'Stir', 'Add scramble', 'Stir', 'Season with salt, sugar, msg here']
  ),
  1
);

