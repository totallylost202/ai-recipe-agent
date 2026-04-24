"""
Suggests a recipe based on user input of one or several ingredients.
Mulituple ingredients are accepted as a tuple.

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
def suggest_recipe(ingredients):
    key = tuple(sorted(ingredients))

    if key in recipes:
        recipe = recipes[key]
        name = recipe["name"]
        calories = recipe["calories"]
        return f"{name}（{calories}kcal）"
    else:
        return "ごめん、見つからない 😢"
    
def main():
    ingredients = input("材料をカンマで入力してね: ").split(",")
    ingredients = [i.strip().lower() for i in ingredients]

    result = suggest_recipe(ingredients)
    print(f"お勧めのレシピ： {result}")


if __name__ == "__main__":
    main()