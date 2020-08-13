
# Write a function with annotations that changes an int into a str.

def int_to_string(num : int) -> str :
    return str(num)

int_to_string()

# Now one that divides an int by another.

def int_divide(num_1 : int, num_2 : int) -> int :
    try:
        #print(num_1 // num_2)
        return num_1 // num_2
    except ZeroDivisionError:
        print('Division by 0!')

int_divide(2,0)

# Annotate the function declaration below.

def send_email(address: str,
               sender : str,
               cc :str,
               cci :str,
               subject='':str,
               body = None : NoneType
               ) -> None:


