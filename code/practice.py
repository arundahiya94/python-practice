# Function as a first class citizen

# 1. Function should be assigned to a variable.

# def firstFunc():
#     print("This is the first function")


# a = firstFunc
# print(a())


# 2. Function should be returnable from a function
# def functA():
#     print("This is the first function ")
#     return functB

# def functB():
#     print("This is the second function")

# a = functA()

# a()


# 3. Function should be passable in a method parameter

# def newFunc(oldFunc):
#     oldFunc()
#     print("This is the new function")

# def oldFunc():
#     print("This is the old function")

# newFunc(oldFunc)

# def outerFunction():
#     print("Entry point of the outer function")
#     def innerFunction():
#         print("Entry point of the inner function")
#         return "return statement of inner function"
    
#     return innerFunction

# a = outerFunction()
# a()


# trialList = [1,2,3,4,5]
# print(trialList)

# def aFunct(varList):
#     varList.append(6)
#     print(varList)

# list is mutable so reference is passed in the function parameter and list is changed
# aFunct(trialList)
# print(trialList)

# x = 10
# print(x)

# def newFunct(var):
#     var = 12
#     print(var)

# integer is immutable so no reference is passed in the function parameter and x is not changed
# newFunct(x)
# print(x)

