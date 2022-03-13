#Lists / Arrays

myList1 = ["banana", "cherry", "apple", "strawberry", "pear", "peach"]         # Create list with elements
myList2 = list()                                # Create empty list
myList3 = [5, True, "apple", "apple"]           # Can contain range of data types and duplicated elements
item1 = myList1[0]                              # How to access individual element, referring to first element
item2 = myList1[-1]                             # Refers to last item, -2 for second to last
myList1[1] = "pineapple"                        # How to change element
for i in myList1:                               # How to iterate through array
    print(i)
if "banana" in myList1:                         # How to check if item is in list
    print("Yes")
else:
    print("No")
len(myList1)                                # How to find length of list
myList1.append("lemon")                     # How to add element to end of list
myList1.insert(1, "blueberry")              # Adds element into position 1
myList1.pop(1)                              # Removes item in position 1
myList1.pop()                               # Removes item at the end of the list
myList1.remove("cherry")                    # Removes item called cherry
myList1.reverse()                           # Reverses the order of the list
myList1.sort()                              # Sorts the list
myList4 = sorted(myList1)                   # Keeps original list and stores sorted one in new list
myList5 = ["banana"] * 5                    # Creates new list with 5 duplicated elements
myList6 = myList1 + myList5                 # Concatenates 2 lists together
myList7 = myList1[1:4]                      # Creates new list with indexes 1,2 and 3 from myList1, not index 4
myList8 = myList1[:4]                       # Creates new list from start of myList1 to index 3, not index 4
myList9 = myList1[2:]                       # Creates new list from index 2 to the end of myList1
myList10 = myList1[::2]                     # Creates new list with every 2nd index from myList1
myList11 = myList1[::-1]                    # Creates new list that is reversed from myList1
myList12 = myList1                          # Copies myList1,however when either one is changed it changes the other
myList13 = myList1.copy()                   # Copies myList1,now when one is changed, the other won't change
myList14 = list(myList1)                    # Copies myList1,now when one is changed, the other won't change
myList15 = myList1[:]                       # Copies myList1,now when one is changed, the other won't change
myList16 = [1, 2, 3, 4, 5]                  # Creates a new list where each element has been squared in new list
myList17 = [x*x for x in myList16]
myList1.clear()                             # Empty the list
