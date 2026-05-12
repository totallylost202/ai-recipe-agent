import streamlit as st
from recipes import suggest_recipe, suggest_random_recipe

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

        display_recipe(data, extra_ingredients)

    else:
        st.error("Please enter ingredients.")


if st.button("🎲 Surprise Me"):

    with st.spinner("Generating random recipe..."):

        data = suggest_random_recipe()

        display_recipe(data)