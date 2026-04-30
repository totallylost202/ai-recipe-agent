from dotenv import load_dotenv

from openai import OpenAI

load_dotenv()

"""

Suggests a recipe based on user input of one or several ingredients, a calorie limit, 
and a number of extra ingredients permitted.

"""


def suggest_recipe(food, calorie_limit, max_extra_ingredients):

        client = OpenAI()

        ingredients_text = ", ".join(food)

        prompt = f"""
        Suggest a vegetarian recipe using: {ingredients_text}. 
        The recipe must be under {calorie_limit} kcal. 
        It can only contain up to {max_extra_ingredients} extra ingredients.
        Create a shopping list of only the extra ingredients."""

        response = client.chat.completions.create(

            model="gpt-4o-mini",

            messages=[

                {"role": "user", "content": prompt}

            ]

        )

        return response.choices[0].message.content

def main():

    food = input("Enter ingredients: ").split(",")

    calorie_limit = int(input("Please set a calorie limit: ")) 

    max_extra_ingredients = int(input("Please set the number of maximum ingredients you'd like to use: "))

    food = [i.strip().lower() for i in food]

    result = suggest_recipe(food, calorie_limit, max_extra_ingredients)

    print(result)

if __name__ == "__main__":

    main()