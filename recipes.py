"""
Suggests a recipe based on user input of one or several ingredients.
Mulituple ingredients are accepted as a tuple.

"""

recipes = {
    ("egg", "rice"): "オムライス",
    ("rice", "tofu"): "豆腐丼",
    ("egg",): "オムレツ",
    ("rice",): "チャーハン",
    ("tofu",): "麻婆豆腐"
}


def suggest_recipe(ingredients):
    key = tuple(sorted(ingredients))
    return recipes.get(key, "ごめん、その材料のレシピはまだない 😢")


def main():
    ingredients = input("材料をカンマで入力してね: ").split(",")
    ingredients = [i.strip().lower() for i in ingredients]

    result = suggest_recipe(ingredients)
    print(f"お勧めのレシピ： {result}")


if __name__ == "__main__":
    main()