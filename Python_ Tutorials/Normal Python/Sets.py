# A set is a list that can be changed and no duplicates possible, unordered and random order
mySet1 = {1, 2, 3}          # How to initialise a set, similar to dictionary but without key value pairs
mySet2 = {1, 2, 3, 1, 2, 4, 5, 6, 7}    # This will only contain {1, 2, 3} as the duplicates are ignored
mySet3 = set("Hello")       # This will create a set with "H", "e", "l" and "o" in a random order, 2nd "l" not in it
myList1 = [1, 2, 3]
mySet4 = set(myList1)       # How to initialise set with list/array
mySet5 = set()              # Only way to make empty set, mySet5 = {} will create a dict
mySet1.add(4)               # How to add element to end of set
mySet1.remove(4)            # How to remove the specified element, but if element doesn't exist, it gives error
mySet1.discard(4)           # How to remove specified element, if element doesn't exist, won't give error, just moves on
mySet3.clear()              # Empties set
mySet2.pop()                # Removes first element from set
for i in mySet2:            # How to iterate over set
    print(i)
if 1 in mySet2:             # How to check if element is in set
    print("yes")
mySet5 = mySet2.union(mySet4)   # Creates set with all elements found in mySet2 and mySet4, removing duplicates
mySet6 = mySet2.intersection(mySet4)    # Creates set with only elements found in both mySet2 and mySet4
mySet7 = mySet2.difference(mySet4)  # Creates set with elements found in mySet3 but not in mySet4
mySet8 = mySet2.symmetric_difference(mySet4)    # Set with elements that appear in either mySet2 or mySet4 but not both
# union, intersection, difference and symmetric difference don't change the original sets
mySet6.update(mySet5)       # Updates mySet6 by adding the elements found in mySet5
mySet6.intersection_update(mySet5)  # Updates mySet6 by keeping only the elements found in both it and mySet5
mySet6.difference_update(mySet5)    # Updates mySet6 by removing elements in mySet6 that are found in mySet7
mySet6.symmetric_difference_update(mySet5)  # Updates mySet6 by having only elements found in either but not both
mySet6.issubset(mySet5)     # Returns true or false depending on whether all elements in mySet6 are found in mySet5
mySet6.issuperset(mySet5)   # Returns true if all elements in mySet5 are found in mySet6
mySet6.isdisjoint(mySet5)   # Returns true if both sets contain no common elements
mySet6 = mySet5             # Duplicates mySet5 into mySet6, any changes to either is also changed on the other
mySet6 = mySet5.copy()      # Duplicates mySet5, but changing 1 doesn't change the other
mySet6 = set(mySet5)        # Duplicates mySet5, but changing 1 doesn't change the other
mySet6 = frozenset([1, 2, 3])   # Creates a set where it cannot be changed after creation
