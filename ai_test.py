from dotenv import load_dotenv

from openai import OpenAI

load_dotenv()

"""

Suggests a recipe based on user input of one or several ingredients. 

Multiple ingredients are accepted as a tuple.

"""

recipes = {

    ("egg", "rice"): {

        "name": "オムライス",

        "calories": 550

    },

    ("rice", "tofu"): {

        "name": "豆腐丼",

        "calories": 500

    },

    ("egg",): {

        "name": "オムレツ",

        "calories": 250

    },

    ("rice",): {

        "name": "チャーハン",

        "calories": 400

    },

    ("tofu",): {

        "name": "麻婆豆腐",

        "calories": 300

    }

}

def suggest_recipe(food, limit):

    total_calories = 0

    results = []

    for key, value in recipes.items():

        if set(food) == set(key) and value["calories"] <= limit:
            
            name = value["name"]

            calories = value["calories"]

            total_calories += value["calories"]

            results.append(f"{name}は{calories}kcalです")

    if results:
        results.append(f"合計：{total_calories}kcal")
        return "\n".join(results)
    

    else:
        client = OpenAI()

        ingredients_text = ", ".join(food)

        prompt = f"Suggest a vegetarian recipe using: {ingredients_text}. The recipe must be under {limit} kcal. Please make a shopping list of ingredients not in {ingredients_text} at the end."

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

    food = [i.strip().lower() for i in food]

    result = suggest_recipe(food, calorie_limit)

    print(result)

if __name__ == "__main__":

    main()