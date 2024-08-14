# List Comprehension

# newlist = [expression for item in iterable if condition == True]

# a = [1,2,3,4,5,6,7,8,9,10]
# print(a)
# print(a[1])
# print(a[1:])
# print(a[:1])

# b= [x for x in range(1,51)]
# print(b)

# c= [ [x] for x in range(1,5)  ]
# print(c)

# e = [ b[x:x+10] for x in range(0,len(b),10)   ]
# print(e)

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
# numbers_plus_one = []
# for number in numbers:
#     numbers_plus_one.append(number + 1)

# print(numbers_plus_one)

# Example of using a list comprehension to create a list of the numbers plus one.
# numbers_plus_one = [number + 1 for number in numbers]
# print(numbers_plus_one)

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
# output = []
# for fruit in fruits:
#     output.append(fruit.upper())

# print(output)


# Exercise 1 - rewrite the above example code using list comprehension syntax. 
# Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]

# uppercased_fruits = [fruit.upper() for fruit in fruits]
# print(uppercased_fruits)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output 
# like ['Mango', 'Kiwi', 'Strawberry', etc...]

# capitalized_fruits = [fruit.capitalize() for fruit in fruits]
# print(capitalized_fruits)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. 
# Hint: You'll need a way to check if something is a vowel.

# fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange', 'appl']

set 
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if len(set(fruit).intersection('aeiou')) >= 2]
print(fruits_with_more_than_two_vowels)

# for fruit in fruits:
#     print(set(fruit).intersection('aeiou'))