# Lambda function is a small, one line function that is defined without a name
# it is formatted as       lambda arguments: expression
add10 = lambda x: x + 10
def add_10(x):                  # These 2 functions do the same thing but lambda is more efficient
    return x + 10

mult = lambda x,y: x*y          # Can be done with multiple arguments

# Can be used to sort lists by specific element
list1 = [(1, 2), (15, 1), (5, -1), (10, 4)]
list1_sorted1 = sorted(list1)   #Sorts by first value by default, outputs   [(1, 2), (5, -1), (10, 4), (15, 1)]
list1_sorted2 = sorted(list1, key=lambda x: x[1])   # Sorts by second value, outputs [(5, -1), (15, 1), (1, 2), (10, 4)]
list1_sorted3 = sorted(list1, key=lambda x: x[0] + x[1])  # Sorts by sum of 2 values, outputs  [(1, 2), (5, -1), (10, 4), (15, 1)]

# can be used as a map function
list2 = [1, 2, 3, 4, 5]
list2_map1 = list(map(lambda x: x*2, list2)) # Creates list2_map1 from each element of list2 *2,outputs [2, 4, 6, 8, 10]
list2_map2 = [x*2 for x in list2]            # Has the same effect as the one above

# filter function
list3 = [1, 2, 3, 4, 5, 6]
list3_filter1 = list(filter(lambda x: x % 2 == 0, list3))  # Only puts the even numbers in list3_filter1, outputs [2, 4, 6]
list3_filter2 = [i for i in list3 if i % 2 == 0]           # Same effect as one above

# reduce function
from functools import reduce
list4 = [1, 2, 3, 4]
list4_product1 = reduce(lambda x,y: x*y, list4) # Outputs single value of all elements multiplied, outputs 24
