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

            data = suggest_recipe(

                food,

                calorie_limit,

                extra_ingredients

            )

        if data["recipe"] == "Error":

            st.error("Something went wrong. Please try again.")

            st.write(data.get("raw_response"))
        
        else:
        
            st.success("Recipe generated!")

            st.subheader(data["recipe"])

            st.write(f'{data["calories"]} kcal')

            st.write("Shopping List:")

            for item in data["shopping_list"]:
                st.write(f"- {item}")

            st.write("Instructions:")

            for step in data["instructions"]:
                st.write(f"- {step}")

    else:
        st.error("Please enter ingredients.")