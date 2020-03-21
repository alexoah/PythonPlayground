"""
from PYTHON Inheritance: Exercise 2 ( https://www.w3schools.com/python/exercise.asp?filename=exercise_inheritance2 )

question:
    We have used the Student class to created an object named x.
    What is the correct syntax to execute the printname method of the object x?

    class Person:
        def __init__(self, fname):
            self.firstname = fname

        def printname(self):
            print(self.firstname)

    class Student(Person):
        pass

    x = Student("Mike")
    _____________
"""
class Person:
    def __init__(self, fname):
        self.firstname = fname

    def printname(self):
        print(self.firstname)

class Student(Person):
    pass

x = Student("Mike")
x.printname()