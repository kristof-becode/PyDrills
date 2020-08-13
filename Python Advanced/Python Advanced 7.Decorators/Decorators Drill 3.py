
import time

def timef(function):
    def wrapper_time(*args,**kwargs):
        start_time = time.perf_counter()
        result = function(*args,**kwargs)
        #print(result) => prints None?????
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(" This function clocked at {} seconds".format(run_time))
        return result
    return wrapper_time
    #print(run_time)

@timef
def fib(n):
    a,b = 0,1
    for i in range(0,n):
        c= a+b
        a,b = b, c
    print(c)
    time.sleep(5)
    return c

fib(13)