"""
from PYTHON Classes: Exercise 4 ( https://www.w3schools.com/python/exercise.asp?filename=exercise_classes4 )

question:
    What is the correct syntax to assign a "init" function to a class?

    class Person:
        def ________ (self, name, age):
            self.name = name
            self.age = age
"""
class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age