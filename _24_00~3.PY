
input_string = input("Enter three numbers separated by a space: ")
inputs = [int(i) for i in input_string.split(' ')]  # eval() creates a list for inputs with format [1,2,3]

def logging_dec(fn):
    def wrapper(*args):
        print(f"You called {fn.__name__} with these arguments: {args}")
        result = fn(args[0], args[1], args[2])  # This line remains unchanged
        print(f"It returned: {result}")
        return result
    return wrapper

@logging_dec
def a_function(a, b, c):
    return a * b * c

a_function(inputs[0], inputs[1], inputs[2])
