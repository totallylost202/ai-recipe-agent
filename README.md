# AI Recipe Agent

A Python AI recipe assistant that suggests vegetarian recipes based on available ingredients, calorie limits, and shopping constraints.

## Features

- Suggests vegetarian recipes
- Uses OpenAI API (gpt-4o-mini)
- Supports:
  - Available ingredients
  - Calorie limits
  - Maximum number of extra ingredients
  - "Surprise Me" mode
  - Save favorite recipes
  - Prevent duplicate saved recipes
  - Search saved recipes by name or ingredients
  - Sort saved recipes by calories
  - Delete saved recipes
- Generates:
  - Recipe suggestions
  - Shopping lists for missing ingredients
- Uses .env for secure API key storage

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

---

## Setup

### 1. Install dependencies

bash python3 -m pip install openai python-dotenv 

### 2. Create a .env file

text OPENAI_API_KEY=your_api_key_here 

### 3. Run the app

bash python3 recipes.py 

---

## Future Improvements

- Protein filtering
- Cuisine selection
- Budget limits
- JSON output formatting
- Streamlit web interface