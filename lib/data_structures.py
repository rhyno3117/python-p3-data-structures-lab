spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]
# Define a function get_names() that takes a list of spicy_foods and returns a 
# list of strings with the names of each spicy food.
def get_names(spicy_foods):
    return [x["name"] for x in spicy_foods]

# Define a function get_spiciest_foods() that takes a list of spicy_foods and returns a list of 
# dictionaries where the heat level of the food is greater than 5.
def get_spiciest_foods(spicy_foods):
    return [x for x in spicy_foods if x["heat_level"] > 5]

# Define a function print_spicy_foods() that takes a list of spicy_foods and output to the terminal 
# each spicy food in the following format using print(): Buffalo Wings (American) | Heat Level: 🌶🌶🌶
def print_spicy_foods(spicy_foods):
    for x in spicy_foods:
        print(f'{x["name"]} ({x["cuisine"]}) | Heat Level: {"🌶" * x["heat_level"]}')

# Define a function get_spicy_food_by_cuisine() that takes a list of spicy_foods and a string 
# representing a cuisine, and returns a single dictionary for the spicy food whose cuisine matches the 
# cuisine being passed to the method.
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

# Define a function print_spiciest_foods() that takes a list of spicy_foods and outputs to the terminal 
# ONLY the spicy foods that have a heat level greater than 5, in the following format:
def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

# Define a function average_heat_level() that takes a list of spicy_foods and returns an integer 
# representing the average heat level of all the spicy foods in the array.
def get_average_heat_level(spicy_foods):
    return sum([food["heat_level"] for food in spicy_foods]) / len(spicy_foods)

# Define a function create_spicy_food() that takes a list of spicy_foods and a new spicy_food and returns the 
# original list with the new spicy_food added.
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
