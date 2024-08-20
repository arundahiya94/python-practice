# Write a program to remove duplicates from a list

def removeDuplicate(inputList):
    print(f"The original list is : {inputList}")
    newSet = set(inputList)
    print(f"The list after duplicate removal is : {newSet}")
    return None

if __name__ == "__main__":

    inputList = [2,2,5,7,3,1,9,10,9]
    removeDuplicate(inputList)