
def check_output(function):
    def wrapper(*args,**kwargs):
        result = function(*args, **kwargs)
        if type(result) == int:
            raise Exception('This function returns an integer!')
        if type(result) == str:
            raise Exception('This function returns a string!')
        return result
    return wrapper

@check_output
def ret_value(n):
    list = ['paper', 45, True, 'laundry', 'pescetarian', False, 987, 876, 'island', 78, True, False, 'kilimanjaro' ] # 13 elements
    print(list[n])
    return list[n]

ret_value(3)
