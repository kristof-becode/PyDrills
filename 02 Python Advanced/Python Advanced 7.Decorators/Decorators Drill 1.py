
def call_limiter(limit):
    def decorator(function):
        def wrapper():
            if wrapper.calls >= limit :
                raise Exception("Enough already, this function ran more than {} times.".format(limit))
            wrapper.calls += 1
            return function()

        wrapper.calls = 0
        return wrapper

    return decorator

@call_limiter(15)
def execute():
    print('Decorators are not that difficult in the end!')

execute()

for i in range(0,30):
    execute()

"""
# you cannot run smthng like a fib loop cause you will never be able to interrupt the loop that's in the function
@call_limiter(3)
def execute():
    a,b = 0,1
    #c = 0
    for i in range(0,100):
        c= a+b
        a,b = b,c
        print(c)

execute()
"""
