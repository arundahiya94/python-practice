# Return the factorial of a number

fact = int(input("Enter the number to calculate factorial: "))

result =1
for i in range(1,fact+1):
    result = result * i

print(f"Factorial of number {fact} is:", result)