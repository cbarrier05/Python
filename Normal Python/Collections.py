# Collections is a module
# Most important parts: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

# Counter
myString1 = "aaaaabbbbccc"
myCounter1 = Counter(myString1)
# This creates a dictionary with counts of the characters in the string
# This example would create a dictionary of {"a": 5, "b": 4, "c": 3}
# You can now treat myCounter1 as a normal dictionary
myCounter1.most_common(1) # Gives most common pair in the dictionary, put 2 in the brackets for the 2 most common
# This creates a list with tuples within
# So type:
myCounter1.most_common(1)[0][0] # To find the most common key, in this case it would be "a"
# First [0] to enter the first tuple in list, Second [0] to enter first element in tuuple, "a" in this case
myList1 = list(myCounter1.elements())   # Lays out each element of the original as a list

# namedtuple
myTuple1 = namedtuple("myTuple1", "x,y")
myItem1 = myTuple1(1,4)     # This sets each provided element, in this case 1 and 4, as a part of myTuple1
# so x is set to 1 and y is set to 4
# print(myItem1) outputs myTuple1(x=1, y=4)

# OrderedDict
# Acts as a regular dictionary, but it remembers the order in which items were added
myOrderedDict1 = OrderedDict()
myOrderedDict1["a"] = 1
myOrderedDict1["b"] = 2
myOrderedDict1["c"] = 3
myOrderedDict1["d"] = 4
# This dictionary is now ordered in order they were added, so "a" first and "d" last
# This is now unnecessary as dictionaries are ordered by default in python 3.7 and later

# defaultdict
myDict1 = defaultdict(str)
myDict1["a"] = 1
myDict1["a"] = 2
# Now if I use a key that doesn't exist, such as "c", it will return the default value for an integer, which is 0
# For float it is 0.0, for string it is "", for list it is []
# It does this instead of giving error

# deque
myDeque1 = deque([10, 11])
# Allows you to use both left and right ends of the list
myDeque1.append(1)              # Appends to right end of myDeque1, [10, 11, 1]
myDeque1.appendleft(2)          # Appends to left end of myDeque1, [2, 10, 11, 1]
myDeque1.pop()                  # Pops from right end, [2, 10, 11]
myDeque1.popleft()              # Pops from left end, [10, 11]
myDeque1.extend([3, 4, 5])      # Extends from right end, [10, 11, 3, 4, 5]
myDeque1.extendleft([6, 7, 8])  # Extends from the left, [10, 11, 3, 4, 5]
myDeque1.rotate(1)              # Move all elements 1 along to the right, [5, 8, 7, 6, 10, 11, 3, 4]
myDeque1.rotate(-2)             # Move all elements 2 along to the left, [7, 6, 10, 11, 3, 4, 5, 8]
