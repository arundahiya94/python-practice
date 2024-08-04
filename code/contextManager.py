# Context Manager

from contextlib import contextmanager

# with open(r".\code\harry_potter_goblet_of_fire.txt") as file:
#     line = file.readline()
#     print(line)


@contextmanager
def random_function():
    print("Inside the random function")
    input = yield 200
    print("Value has been yielded and this line is printed due to context manager")
    print(f"sent value is {input}")

with random_function() as value:
    print(f"The Yielded value is {value}")