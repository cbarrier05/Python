# Uses Key-value pairs,
myDict1 = {"name": "Max", "age": 28, "city": "New York"}    # Creating dictionary
myDict2 = dict(name="Mark", age=27, phone="01403 753693")     # Another way to create
value1 = dict["name"]                                   # Gives the value of what is in "name", in this case "Max"
myDict1["email"] = "max@xyz.com"                        # Adds another value to dictionary under name "email"
myDict1["email"] = "coolmax@xyz.com"                    # Also used to override the value in the "email" section
del myDict2["name"]                                     # Removes the "name" key value pair
myDict2.pop("age")                                      # Removes the "age" key value pair
myDict2.popitem()                                       # Removes the last ey value pair
if "name" in myDict1:                                   # Checks if there is a name key value pair
    print(myDict1["name"])                              # then if there is it prints what is in it
try:                                                    # Checks if there is name key pair, then prints contents
    print(myDict1["lastname"])                          # if not it prints "Error"
except:
    print("Error")
for key in myDict1.keys():                              # Iterates through the key value names, "name, "age" etc
    print(key)
for value in myDict1.values():                          # Iterates through the key value values, "Max", 28, etc
    print(value)
for key, value in myDict1.items():                      # Iterates through both the names and values
    print(key, value)
myDict3 = myDict1                                       # Copies dict, however when change one, it changes other as well
myDict4 = dict(myDict1)                                 # Copies dict, when one change, it doesn't change the other
myDict1.update(myDict2)                                 # Updates myDict1 by adding or overwriting the data that exists
# in myDict2. So changes "name" to "Mark", changes "age" to 27, keeps "city" the same as nothing to overwrite it
# keeps "email" the same as nothing to overwrite it, adds "phone" at the end

# You can use many data types as a value, such as an integer, or even a tuple but not a list
myTuple = (0, 1)
myDict5 = {myTuple: "Example", 12: "Example2"}