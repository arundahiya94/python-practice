# Swap two numbers

# First number greater than 10
# Second number greater than 20
# If both conditions not true then print (both conditions not met)
# If number 1 less than 10 
# If number 2 less than 20

# Solution
a = int(input("Enter the first number: \n"))
b = int(input("Enter the second number: \n"))
print("First number is: ", a)
print("Second number is: ", b)

if a <= 10 and b <= 20:
    print("Both conditions not met")
elif a <= 10:
    print("First number should be greater than 10")
elif b <= 20:
    print("Second number should be greater than 20")
else:
    a = a + b
    b = a - b
    a = a - b
    print("First number is: ", a)
    print("Second number is: ", b)

