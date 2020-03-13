"""
from PYTHON Variables: Exercise 7 ( https://www.w3schools.com/python/exercise.asp?filename=exercise_variables7 )

question:
    Insert the correct keyword to make the variable x belong to the global scope.

    def myfunc():
        ______ x
        x = "fantastic"
"""
def myfunc():
    global x
    x = "fantastic"