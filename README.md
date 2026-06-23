# AI Recipe Agent

A Python AI recipe assistant that suggests vegetarian recipes based on available ingredients, calorie limits, and shopping constraints.

## Features

- Suggests vegetarian recipes
- Uses OpenAI API (gpt-4o-mini)
- Uses .env for secure API key storage
- Supports:
  - Available ingredients
  - Calorie limits
  - Maximum number of extra ingredients
  - "Surprise Me" mode
  - Save favorite recipes
  - Prevent duplicate saved recipes
  - Sort saved recipes by calories
  - Delete saved recipes
  - Use session state for recipe controls
  - Cuisine, mood, and difficulty controls
  - Save notes for saved recipes
  - Add, display, and search tags for saved recipes
  - Search saved recipes by name, ingredients, shopping list, or tags
  - Reset recipe controls and saved recipe filters

- Generates:
  - Recipe suggestions
  - Shopping lists for missing ingredients

---

## Example

### Input

text Ingredients: egg, rice Calorie limit: 600 Maximum extra ingredients: 2 

### Output

text Egg Fried Rice Bowl  Ingredients: - egg - rice - soy sauce - green onion  Instructions: 1. Cook the rice... 2. Fry the egg...  Shopping List: - soy sauce - green onion 

---

## Technologies Used

- Python
- OpenAI API
- dotenv (python-dotenv)
- Dictionaries
- Functions
- Loops and conditionals
- Streamlit
- JSON


---

## Setup

### 1. Install dependencies

python3 -m pip install openai python-dotenv streamlit

### 2. Create a .env file

text OPENAI_API_KEY=your_api_key_here 

### 3. Run the app

streamlit run app.py 

---

## Future Improvements

- Protein filtering
- Budget limits
