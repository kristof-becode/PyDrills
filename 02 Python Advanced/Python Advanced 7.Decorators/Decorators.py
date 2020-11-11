"""
# /////////////// simple decorator that returns function and name
def decorator(f):
    print(f.__name__)
    return f

@decorator
def addition(a, b):
    print(a+b)
    return a + b

addition(5,6)

"""
# ///////////////a bit more complicated..:
def print_decorator(function):
    def new_function(a, b): # New function behaving as the function to be decorated
        print('Add of numbers {} and {}'.format(a, b))
        ret = function(a, b) # Call to function
        print('Return: {}'.format(ret))
        return ret
    return new_function # don't forget to return new function

@print_decorator
def addition(a, b):
    return a + b

addition(1, 2)

#returns:
# Add of numbers 1 and 2
# Return: 3



