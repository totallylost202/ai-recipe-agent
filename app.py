import streamlit as st
from recipes import suggest_recipe, suggest_random_recipe, save_favorite, load_favorites, delete_favorite

def display_recipe(data, extra_ingredients=None):
    if data["recipe"] == "Error":
        st.error("Something went wrong. Please try again.")
        st.write(data.get("raw_response"))
    else:
        st.success("Recipe generated!")

        st.subheader(data["recipe"])

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Calories", data["calories"])

        st.subheader("🥕 Ingredients")

        for item in data["ingredients"]:
            st.write(f"- {item}")

        if extra_ingredients is not None:
            with col2:
                st.metric("Extra ingredients", extra_ingredients)

        st.subheader("🛒 Shopping List")
        with st.expander("Show Shopping List"):
            for item in data["shopping_list"]:
                st.write(f"- {item}")

        st.subheader("👩‍🍳 Instructions")
        for step in data["instructions"]:
            st.write(f"- {step}")

        if st.button("Save recipe"):
            save_favorite(st.session_state["current_recipe"])
            st.session_state["saved"] = True

        if st.session_state.get("saved"):
            st.success("Recipe saved!")

if "current_recipe" not in st.session_state:

    st.session_state["current_recipe"] = None

if "saved" not in st.session_state:

    st.session_state["saved"] = False

st.title("AI Recipe Agent")

ingredients = st.text_input("Enter ingredients", placeholder="egg, rice, tofu")

calorie_limit = st.number_input("Calorie limit", min_value=100, step=50)

extra_ingredients = st.number_input(

    "Maximum extra ingredients",

    min_value=0,

    step=1

)

cuisine = st.selectbox(

    "Cuisine",

    ["Any", "Japanese", "Italian", "Indian", "Healthy"]

)

mood = st.selectbox(

    "Mood",

    ["Any", "Comfort food", "High protein", "Low calorie", "Quick meal", "Budget-friendly"]

)

difficulty = st.radio(

    "Difficulty",

    ["Easy", "Medium", "Hard"]

)

if st.button("Generate Recipe"):

    if ingredients:

        food = [i.strip().lower() for i in ingredients.split(",")]

        with st.spinner("Generating recipe..."):

            data = suggest_recipe(
                food,
                calorie_limit,
                extra_ingredients,
                cuisine,
                mood,
                difficulty
            )

        
        st.session_state["current_recipe"] = data

        st.session_state["saved"] = False


    else:
        st.error("Please enter ingredients.")


if st.button("🎲 Surprise Me"):

    with st.spinner("Generating random recipe..."):

        data = suggest_random_recipe()

        st.session_state["current_recipe"] = data

        st.session_state["saved"] = False


if st.session_state["current_recipe"]:

    display_recipe(
        st.session_state["current_recipe"],
        extra_ingredients
    )

if st.button("🔄 Reset"):

    st.session_state["current_recipe"] = None

    st.session_state["saved"] = False

    st.rerun()


with st.expander("📚 Saved recipes"):
    favorites = load_favorites()
    displayed_recipes = []
    search_word = st.text_input("Search saved recipes")
    if search_word:
        for recipe in favorites:
            if search_word.lower() in recipe["recipe"].lower():
                displayed_recipes.append(recipe)
    else:
        displayed_recipes = favorites
    if displayed_recipes:
        for recipe in displayed_recipes:
            with st.expander(recipe["recipe"]):
                st.write(f"🔥 {recipe['calories']} kcal")
                st.subheader("🥕 Ingredients")
                for item in recipe["ingredients"]:
                    st.write(f"- {item}")
                st.subheader("👩‍🍳 Instructions")
                for step in recipe["instructions"]:
                    st.write(f"- {step}")
                st.subheader(f"🛒 Shopping List")
                for item in recipe["shopping_list"]:
                    st.write(f"- {item}")

                if st.button(
                    "Delete",
                    key=f"delete_{recipe['recipe']}"
                    ):

                    delete_favorite(recipe["recipe"])

                    st.success("Recipe deleted!")

                    st.rerun()
    else:
        st.write("No matching recipes.")