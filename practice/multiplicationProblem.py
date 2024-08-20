# Write a program that give the multiplication table of a given number

def tableCalculator(num, ranze):
    for i in range(1, ranze +1):
        val = i * num
        print(f"{i} X {num} = {val}")


if __name__ == "__main__":
    num = int(input("Enter the number: "))
    ranze = int(input("Enter the range: "))
    tableCalculator(num, ranze)

