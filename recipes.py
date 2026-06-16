"""

Suggests a recipe based on user input of one or several ingredients, a calorie limit, 
and a number of extra ingredients permitted.

"""

from dotenv import load_dotenv

from openai import OpenAI

import json

load_dotenv()

client = OpenAI()


def parse_response(response):

    content = response.choices[0].message.content

    try:

        return json.loads(content)

    except json.JSONDecodeError:

        return {

            "recipe": "Error",

            "calories": 0,

            "ingredients": [],

            "shopping_list": [],

            "instructions": ["Failed to parse AI response."],

            "note": "",

            "raw_response": content

        }

def suggest_recipe(food, calorie_limit, max_extra_ingredients, cuisine, mood, difficulty):

    ingredients_text = ", ".join(food)

    prompt = f"""
    Suggest a vegetarian recipe using: {ingredients_text}. 
    The recipe must be under {calorie_limit} kcal. 
    It can only contain up to {max_extra_ingredients} extra ingredients.
    The cuisine should be {cuisine}.
    The mood/style should be: {mood}.
    The difficulty should be: {difficulty}.
    Create a shopping list of only the extra ingredients.
    Include step-by-step cooking instructions.

    Return the result in JSON format.

    Use this structure:

    {{

        "recipe": "",

        "calories": 0,

        "ingredients": [],

        "shopping_list": [],

        "instructions": []

    }}

    Return ONLY valid JSON.
    Do not use markdown.
    Do not use code blocks.

    """

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[

            {"role": "user", "content": prompt}

        ]

    )

    return parse_response(response)
    
def suggest_random_recipe():
    prompt = f"""
    Suggest a vegetarian recipe.
    Create a shopping list of necessary ingredients.
    Include step-by-step cooking instructions.

    Return the result in JSON format.

    Use this structure:

    {{

        "recipe": "",

        "calories": 0,

        "ingredients": [],

        "shopping_list": [],

        "instructions": []

    }}

    Return ONLY valid JSON.
    Do not use markdown.
    Do not use code blocks.

    """

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[

            {"role": "user", "content": prompt}

        ]

    )

    return parse_response(response)


def save_favorite(recipe_data):

    try:
        with open("favorites.json", "r") as f:
            favorites = json.load(f)

    except FileNotFoundError:
        favorites = []

    except json.JSONDecodeError:
        favorites = []

    favorites.append(recipe_data)

    with open("favorites.json", "w") as f:
        json.dump(favorites, f, indent=2)

def load_favorites():

    try:
        with open("favorites.json", "r") as f:
            return json.load(f)
        
    except FileNotFoundError:
        return []
    
    except json.JSONDecodeError:
        return []

def delete_favorite(recipe_name):

    try:

        with open("favorites.json", "r") as f:

            favorites = json.load(f)

    except FileNotFoundError:

        favorites = []

    except json.JSONDecodeError:

        favorites = []

    new_favorites = []

    for recipe in favorites:

        if recipe["recipe"] != recipe_name:

            new_favorites.append(recipe)

    with open("favorites.json", "w") as f:

        json.dump(new_favorites, f, indent=2)

def add_note_to_favorite(recipe_name, note):

    try:

        with open("favorites.json", "r") as f:

            favorites = json.load(f)

    except FileNotFoundError:

        favorites = []

    except json.JSONDecodeError:

        favorites = []

    for recipe in favorites:
        if recipe["recipe"] == recipe_name:
            recipe["note"] = note
        
    with open("favorites.json", "w") as f:
        json.dump(favorites, f, indent=2)

def main():

    food = input("Enter ingredients: ").split(",")

    calorie_limit = int(input("Please set a calorie limit: ")) 

    max_extra_ingredients = int(input("Please set the maximum number of ingredients you'd like to use: "))

    cuisine = input("Please choose a cuisine: ")

    mood = input("Mood: ")

    difficulty = input("Difficulty: ")

    food = [i.strip().lower() for i in food]

    result = suggest_recipe(food, calorie_limit, max_extra_ingredients, cuisine, mood, difficulty)

    print(result)

if __name__ == "__main__":

    main()