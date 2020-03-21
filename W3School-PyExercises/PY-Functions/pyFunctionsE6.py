"""
from PYTHON Functions: Exercise 6 ( https://www.w3schools.com/python/exercise.asp?filename=exercise_functions6 )

question:
    If you do not know the number of keyword arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?

    def my_function(__kid):
        print("His last name is " + kid["lname"])
"""
def my_function(**kid):
    print("His last name is " + kid["lname"])