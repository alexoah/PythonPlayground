"""
from PYTHON While Loops: Exercise 3 ( https://www.w3schools.com/python/exercise.asp?filename=exercise_while_loops3 )

question:
    In the loop, when i is 3, jump directly to the next iteration.

    i = 0
    while i < 6:
        i += 1
        if i == 3:
            ________
        print(i)
"""
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)