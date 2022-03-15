# 2 types
# Function Decorators:

# Allows you to add extra actions to
# subroutine without modifying original

def start_end_decorator(function):
    def wrapper():
        print("Start")
        function()
        print("End")
    return wrapper
@start_end_decorator  # This line combines print_name with the decorator
def print_name():
    print("Christian")

print_name()       # Now this has the combined function of both
                   # Outputs "Start Christian End"
# Therefore can extend behaviour of print_name() without changing original

def decorator1(function):
    def wrapper(*args, **kwargs):
        print(function(*args, **kwargs))
    return wrapper
@decorator1      # If parameters in original, need to add (*args, **kwargs)
def add5(x):     # into the decorator function
    return x + 5
add5(10)


def decorator2(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result   # How to return from the decorator
    return wrapper
@decorator2
def add10(x):
    return x + 10
answer = add10(10)


# Class decorator

class CountCalls:
    def __init__(self,function):
        self.function = function
        self.num_calls = 0
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print({self.num_calls}, "times")

@CountCalls
def say_hello():
    print("Hello")