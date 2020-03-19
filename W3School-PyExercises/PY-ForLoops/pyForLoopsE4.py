"""
from PYTHON For Loops: Exercise 4 ( https://www.w3schools.com/python/exercise.asp?filename=exercise_for_loops4 )

question:
    Exit the loop when x is "banana".

    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        if x == "banana":
            _____
        print(x)
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)