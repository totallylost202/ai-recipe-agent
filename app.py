import streamlit as st
from recipes import suggest_recipe, suggest_random_recipe, save_favorite, load_favorites, delete_favorite, add_note_to_favorite, add_tags_to_favorite


def display_recipe(data, extra_ingredients=None):
    if data["recipe"] == "Error":
        st.error("Something went wrong. Please try again.")
        st.write(data.get("raw_response"))
    else:
        st.success("Recipe generated!")

        st.subheader(data["recipe"])

        metric_col1, metric_col2 = st.columns(2)

        with metric_col1:
            st.metric("Calories", data["calories"])

        if extra_ingredients is not None:
            with metric_col2:
                st.metric("Extra ingredients", extra_ingredients)

        st.subheader("🥕 Ingredients")
        with st.expander("Show Ingredients"):
            for item in data["ingredients"]:
                st.write(f"- {item}")

        st.subheader("🛒 Shopping List")
        with st.expander("Show Shopping List"):
            for item in data["shopping_list"]:
                st.write(f"- {item}")

        st.subheader("👩‍🍳 Instructions")
        for step in data["instructions"]:
            st.write(f"- {step}")

        if st.button("Save recipe"):
            current_recipe_name = st.session_state["current_recipe"]["recipe"]
            favorites = load_favorites()
            already_saved = any(
                recipe["recipe"] == current_recipe_name
                for recipe in favorites
            )
            if already_saved:
                st.warning("Already saved!")
            else:
                save_favorite(st.session_state["current_recipe"])
                st.toast("Recipe saved!")


# Reset function for the app
def reset_app():
    st.session_state["current_recipe"] = None
    st.session_state["saved"] = False
    st.session_state["cuisine"] = "Any"
    st.session_state["mood"] = "Any"
    st.session_state["difficulty"] = "Easy"
    st.session_state["ingredients"] = ""
    st.session_state["calorie_limit"] = 100
    st.session_state["extra_ingredients"] = 0


def reset_favorites_search():
    st.session_state["search_word"] = ""
    st.session_state["sort_order"] = "Low to High"


if "current_recipe" not in st.session_state:
    st.session_state["current_recipe"] = None

if "saved" not in st.session_state:
    st.session_state["saved"] = False

if "calorie_limit" not in st.session_state:
    st.session_state["calorie_limit"] = 100

if "extra_ingredients" not in st.session_state:
    st.session_state["extra_ingredients"] = 0

if "ingredients" not in st.session_state:
    st.session_state["ingredients"] = ""

if "mood" not in st.session_state:
    st.session_state["mood"] = "Any"

if "difficulty" not in st.session_state:
    st.session_state["difficulty"] = "Easy"

if "cuisine" not in st.session_state:
    st.session_state["cuisine"] = "Any"

st.title("AI Recipe Agent")

st.text_input("Enter ingredients", placeholder="egg, rice, tofu", key="ingredients")

st.number_input("Calorie limit", min_value=100, step=50, key="calorie_limit")

st.number_input(
    "Maximum extra ingredients",
    min_value=0,
    step=1,
    key="extra_ingredients"
)

st.selectbox(
    "Cuisine",
    ["Any", "Japanese", "Italian", "Indian", "Healthy"],
    key="cuisine"
)

st.selectbox(
    "Mood",
    ["Any", "Comfort food", "High protein", "Low calorie", "Quick meal", "Budget-friendly"],
    key="mood"
)

st.radio(
    "Difficulty",
    ["Easy", "Medium", "Hard"],
    key="difficulty"
)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Generate Recipe"):
        if st.session_state["ingredients"]:
            food = [i.strip().lower() for i in st.session_state["ingredients"].split(",")]

            with st.spinner("Generating recipe..."):
                data = suggest_recipe(
                    food,
                    st.session_state["calorie_limit"],
                    st.session_state["extra_ingredients"],
                    st.session_state["cuisine"],
                    st.session_state["mood"],
                    st.session_state["difficulty"]
                )

            st.session_state["current_recipe"] = data
            st.session_state["saved"] = False
        else:
            st.error("Please enter ingredients.")

with col2:
    if st.button("🎲 Surprise Me"):
        with st.spinner("Generating random recipe..."):
            data = suggest_random_recipe()
            st.session_state["current_recipe"] = data
            st.session_state["saved"] = False

if st.session_state["current_recipe"]:
    display_recipe(
        st.session_state["current_recipe"],
        st.session_state["extra_ingredients"]
    )

with col3:
    st.button("🔄 Reset", on_click=reset_app, key="reset_app")

def display_recipe_information(recipe):
    st.write(f"🔥 {recipe['calories']} kcal")

    st.subheader("🥕 Ingredients")
    with st.expander("Show Ingredients"):
        for item in recipe["ingredients"]:
            st.write(f"- {item}")

    st.subheader("👩‍🍳 Instructions")
    for step in recipe["instructions"]:
        st.write(f"- {step}")

    st.subheader("🛒 Shopping List")
    with st.expander("Show Shopping List"):
        for item in recipe["shopping_list"]:
            st.write(f"- {item}")

def display_note(recipe, note_key):
    st.text_area(
        "Note",
        value=recipe.get("note", ""),
        key=note_key
    )

def display_saved_tags(recipe, tags_key):

    st.text_input("Add tags", value=", ".join(recipe.get("tags", [])), key=tags_key)

    tags_list = recipe.get("tags", [])

    if tags_list:
        st.write("🏷️ " + " | ".join(tags_list))
    else:
        st.write("No tags yet.")


def clear_note(recipe, note_key):
    add_note_to_favorite(recipe["recipe"], "")
    st.session_state[note_key] = ""
    st.toast("Note cleared.")


def clear_tags(recipe, tags_key):
    add_tags_to_favorite(recipe["recipe"], [])
    st.session_state[tags_key] = ""
    st.toast("Tags cleared.")



def display_saved_recipe_card(recipe):
    with st.expander(recipe["recipe"]):
        
        display_recipe_information(recipe)

        st.subheader("Personal Notes")

        note_key = f"note_{recipe['recipe']}"
        
        display_note(recipe, note_key)

        col4, col5 = st.columns(2)

        with col4:
            if st.button(
                "Save note",
                key=f"save_note_{recipe['recipe']}"
            ):
                add_note_to_favorite(recipe["recipe"], st.session_state[note_key])
                st.toast("Note saved!")

        with col5:
            st.button(
                "Clear note",
                on_click=clear_note,
                args=(recipe, note_key),
                key=f"clear_note_{recipe['recipe']}"
            )

        tags_key = f"tags_{recipe['recipe']}"

        display_saved_tags(recipe, tags_key)
        
        col6, col7 = st.columns(2)

        with col6:
            if st.button(
                "Save tags",
                key=f"save_tags_{recipe['recipe']}"
            ):
                tags = [
                    tag.strip()
                    for tag in st.session_state[tags_key].split(",")
                    if tag.strip()
                ]

                add_tags_to_favorite(recipe["recipe"], tags)
                st.toast("Tags saved!")

        with col7:
            st.button(
                "Clear tags",
                on_click=clear_tags,
                args=(recipe, tags_key),
                key=f"clear_tags_{recipe['recipe']}"
            )

        if st.button(
            "🗑️ Delete recipe",
            key=f"delete_{recipe['recipe']}"
        ): 
            delete_favorite(recipe["recipe"])
            st.rerun()

def display_saved_recipes():
    favorites = load_favorites()
    if not favorites:
        st.write("No saved recipes.")
    else:
        with st.expander(f"📚 Saved recipes ({len(favorites)})"):

            if "search_word" not in st.session_state:
                st.session_state["search_word"] = ""

            if "sort_order" not in st.session_state:
                st.session_state["sort_order"] = "Low to High"

            st.text_input(
                "Search saved recipes",
                key="search_word"
            )

            search_text = st.session_state["search_word"].lower()

            displayed_recipes = [
                recipe
                for recipe in favorites
                if (
                    search_text in recipe["recipe"].lower()
                    or search_text in " ".join(recipe["ingredients"]).lower()
                    or search_text in " ".join(recipe["shopping_list"]).lower()
                    or search_text in " ".join(recipe.get("tags", [])).lower()
                )
            ]

            st.selectbox(
                "Order",
                ["Low to High", "High to Low"],
                key="sort_order"
            )

            st.button(
                "🔄 Reset saved filters",
                on_click=reset_favorites_search,
                key="reset_saved_filters"
            )

            displayed_recipes = sorted(
                displayed_recipes,
                key=lambda recipe: recipe["calories"],
                reverse=st.session_state["sort_order"] == "High to Low"
            )

            if displayed_recipes:
                if search_text:
                    if len(displayed_recipes) == 1:
                        st.write("1 recipe found!")
                    else:
                        st.write(f"{len(displayed_recipes)} recipes found!")

                for recipe in displayed_recipes:
                    display_saved_recipe_card(recipe)
            else:
                st.write("No matching recipes.")


display_saved_recipes()