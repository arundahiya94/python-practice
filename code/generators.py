#Generators
def generator_func(value):
    print("Inside generator function")
    count = 0

    while count < value:
        print("Waiting before the yield statement")
        yield count
        print("Yield statement executed")
        count += 1

for value in generator_func(3):
    print(value)

# generator = generator_func(3)
# # print(generator)
# print(generator.__next__())
# print(generator.__next__())
# print(generator.__next__())
# # print(generator.__next__())