"""
Make a dictionary of recipes and suggest a recipe using an inputted ingredient 

"""

def suggest_recipe(ingredient):

    recipes = {

        "tofu": "麻婆豆腐",

        "egg": "オムレツ",

        "rice": "チャーハン"

    }

    if ingredient in recipes:

        return f"{ingredient}を使うレシピ：{recipes[ingredient]}"

    else:

        return "ごめん、その材料のレシピはまだない 😢"

def main():

    ingredient = input("使いたい材料は？（英語で）").strip().lower()

    result = suggest_recipe(ingredient)

    print(result)

if __name__ == "__main__":

    main()