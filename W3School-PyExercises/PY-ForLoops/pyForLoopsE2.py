"""
from PYTHON For Loops: Exercise 2 ( https://www.w3schools.com/python/exercise.asp?filename=exercise_for_loops2 )

question:
    In the loop, when the item value is "banana", jump directly to the next item.

    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        if x == "banana":
            ________
        print(x)
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)