# Tuple is similar to list but cannot be changed after creation
# More efficient than a list with large data
myTuple1 = ("Max", 28, "Boston")            # To make a Tuple
myTuple2 = ("Max",)                         # To make a Tuple with 1 element, needs the comma
myTuple3 = tuple(["Max", 28, "Boston"])     # To make a Tuple out of already existing list
item1 = myTuple1[0]                         # To find element 0 of Tuple
item2 = myTuple1[-1]                        # To find last element, -2 for second to last

# Cannot change Tuple, e.g. myTuple1[0] = "Tim", doesn't work

for i in myTuple2:                          # To iterate through Tuple
    print(i)
if "Max" in myTuple1:                       # How to check if item is in Tuple
    print("Yes")
else:
    print("No")
len(myTuple1)                               # To find length of Tuple
myTuple4 = ("a", "p", "p", "l", "e")
myTuple4.count("p")                         # Checks how many "p"s are in Tuple, 2 in this case
myTuple4.index("p")                         # Returns index of first "p" in Tuple, 1 in this case
myList1 = list(myTuple4)                    # Creates list from content of Tuple
myTuple5 = tuple(myList1)                   # Creates Tuple from content of list
myTuple6 = myTuple4[1:4]                    # Creates Tuple of indexes 1, 2 and 3 from myTuple4, not including index 4
myTuple7 = myTuple4[:4]                     # Creates Tuple of all indexes from start up to but not including index 4
myTuple8 = myTuple4[2:]                     # Creates Tuple of all indexes from index 2 and upwards
myTuple9 = myTuple4[::2]                    # Creates Tuple with every 2nd index from myTuple4
myTuple10 = myTuple4[::-1]                  # Creates Tuple with reverse of myTuple4, e.g. ("e", "l", "p", "p", "a")
myTuple11 = ("Christian", 16, "Ifold")
name, age, village = myTuple11              # Sets each element of myTuple11 to each of the variables
# Needs same number of variables as elements in myTuple11
myTuple12 = (0, 1, 2, 3, 4, 5)
i1, *i2, i3 = myTuple12                     # Sets i1 as first element, i3 as last and i2 as a list of all in between
