# Decorator Example

def outer_function(func):
    print("Inside outer function")
    def inner_function(*args,**kwargs):
        print("Inside inner function")
        var = func(*args,**kwargs) # var = string_function()
        print("String function executed")
        upper_case = var.upper()
        return upper_case
    
    return inner_function


@outer_function
def string_function():
    print("Inside the string function")
    return "hello i am lower case sentence"

print(string_function())


