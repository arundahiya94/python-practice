# Coroutines Example

def outer_function(func):
    print("Inside the decorated outer function")
    def inner_function(*args,**kwargs):
        print("Inside the inner function")
        var = func(*args,**kwargs)
        var.__next__()
        return var
    return inner_function


@outer_function
def some_function():
    print("Inside some function before yield statement")
    input = yield
    print(f"The Yielded value is {input}") 
    yield

result = some_function()
print("Haven't called send yet")
result.send(100)