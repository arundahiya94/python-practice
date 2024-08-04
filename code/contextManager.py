# Context Manager

from contextlib import contextmanager

# with open(r".\code\harry_potter_goblet_of_fire.txt") as file:
#     line = file.readline()
#     print(line)


@contextmanager
def random_function():
    print("Inside the random function")
    yield 200
    print("Value has been yielded and this line is printed due to context manager")

with random_function() as value:
    print(f"The Yielded value is {value}")


file_container = []
for x in range(100000):
    with open(r".\code\harry_potter_goblet_of_fire.txt") as file:
        file_container.append(file)
