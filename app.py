import streamlit as st
from recipes import suggest_recipe

st.title("AI Recipe Agent")

ingredients = st.text_input("Enter ingredients", placeholder="egg, rice, tofu")

calorie_limit = st.number_input("Calorie limit", min_value=100, step=50)

extra_ingredients = st.number_input(

    "Maximum extra ingredients",

    min_value=0,

    step=1

)

if st.button("Generate Recipe"):

    if ingredients:

        food = [i.strip().lower() for i in ingredients.split(",")]

        with st.spinner("Generating recipe..."):

            result = suggest_recipe(

                food,

                calorie_limit,

                extra_ingredients

            )

        st.success(result)

    else:

        st.error("Please enter ingredients.")