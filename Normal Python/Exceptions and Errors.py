# Syntax error occurs when the word order is incorrect
# such as a = 5 print(a)    , need to use a new line for print(a) instead
# or print(a))      , this would count as a syntax error as well

# Exception is when there isn't anything syntaxly wrong with the statement. There are multiple classes of them
# trying to concatenate and int and string will give a TypeError
# importing a module that doesn't exist will cause a ModuleNotFoundError
# b = c when c not defined, gives a NameError
# open("somefile.txt") when file doesn't exist, gives a FileNotFoundError
# a = [1,2,3]   a.remove(4)  , when right data type but wrong value, gives a ValueError
# a = [1,2,3] a[4] , when index not in it, gives IndexError
# dict = {"name": "Max"}    dict["age"] when "age" doesn't exist, gives a KeyError

# Raising an exception
x = -5
if x < 0:
    raise Exception("x should be more than 0")      # Allows to raise a custom exception whenever you want

# Assertion
i = -5
assert(x >= 0), "x is not positive"    # Raises an AssertionError and prints message , as assertion not true

# Catching exceptions
try:
    a = 5 / 0       # This will raise an error as / 0 not allowed
except:             # If exception raised, code continues here
    print("An error occured")
# Good practise to specify the error type
try:
    b = 5 / 0
except ZeroDivisionError as e:
    print(e)                            # Prints what the error is
# Can be set up to handle different types of errors
try:
    c = 5 / 1
    d = c + "10"                        # Allows different outcomes for each type of error expected
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
# Can use else for if no error
try:
    f = 5 / 1
    g = f + 4
except ZeroDivisionError as e:          # So if no error occurs it enters else
    print(e)
except TypeError as e:
    print(e)
else:
    print("Everything is fine")
# finally runs no matter whether there is an error or not
try:
    h = 5 / 1
    i = h + 4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("Everything is fine")         # finally runs everytime
finally:
    print("Check finished")


# How to define your own error class
class ValueTooHighError(Exception):
    pass
# New error type now set as a ValueTooHighError
# This can now be used like any other error type
def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high")
