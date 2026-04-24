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

def suggest_recipe(food):

    results = []

    for key, value in recipes.items():

        if all(i in food for i in key):

            name = value["name"]

            calories = value["calories"]

            results.append(f"{name}は{calories}kcalです")

    if results:

        return "\n".join(results)

    else:

        return "Not found"

def main():

    food = input("Enter ingredients: ").split(",")

    food = [i.strip().lower() for i in food]

    result = suggest_recipe(food)

    print(result)

if __name__ == "__main__":

    main()