"""
from PYTHON Dictionaries: Exercise 1 ( https://www.w3schools.com/python/exercise.asp?filename=exercise_dictionaries1 )

question:
    Use the get method to print the value of the "model" key of the car dictionary.

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print(____________)
"""
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.get("model"))