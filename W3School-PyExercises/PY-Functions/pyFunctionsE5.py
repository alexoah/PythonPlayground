"""
from PYTHON Functions: Exercise 5 ( https://www.w3schools.com/python/exercise.asp?filename=exercise_functions5 )

question:
    If you do not know the number of arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?

    def my_function(_kids):
        print("The youngest child is " + kids[2])
"""
def my_function(*kids):
    print("The youngest child is " + kids[2])