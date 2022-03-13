# module for handling iterators.
# Iterators are data types that can be used in a for loop, such as a list
# Module includes: product, permutations, combinations, accumulate, groupby and infinite iterators
from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import accumulate
import operator
from itertools import groupby
from itertools import count, cycle, repeat


# product
list1 = [1, 2]
list2 = [3, 4]
product = list(product(list1, list2))   # Combines each element of the arrays, output [(1, 3), (1, 4), (2, 3), (2, 4)]
# product2 = list(product(list1, list2, repeat=2))  # Repeat changes how many times it multiplies for each element

# permutations
list3 = [1, 2, 3]
perm = list(permutations(list3))    # Gives a list of all possible orderings
# print(perm)                         # Outputs [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
perm2 = list(permutations(list3, 2))    # Gives a list of all possible outcomes with 2 elements per outcome
# print(perm2)                        # Outputs [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# combinations
list4 = [1, 2, 3, 4]
comb = list(combinations(list4, 2))  # Similar to permutations but no duplicates and only one combination of each set
# print(comb)             # e.g if does (1,2) won't do (2,1) Outputs [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# accumulate
list5 = [1, 2, 3, 4]
acc = list(accumulate(list5))   # Adds elements to each other as it goes, cumulative frequency
# print(acc)                      # Outputs [1, 3, 6, 10]
acc2 = list(accumulate(list5, func=operator.mul))   # If import operator you can change what it does as it goes
# print(acc2)         # This multiplies as it goes, outputs [1, 2, 6, 24]
list6 = [1, 2, 5, 3, 4]
acc3 = list(accumulate(list6, func=max))   # Records the max as it goes along, outputs [1, 2, 5, 5, 5]

# groupby
list7 = [1, 2, 3, 4]
def smallerthan3(x):
    return x < 3
group_obj = groupby(list7, key=smallerthan3)    # Allows to group data into key value pairs
# group_obj = groupby(list7, key=lambda x: x<3)   # Does same thing
for key, value in group_obj:        # Outputs which are in the group of smaller than 3 and which aren't
    print(key, list(value))         # Outputs True [1, 2]   False [3, 4]

persons = [{"name": "Tim", "age": 25}, {"name": "Dan", "age": 25},
           {"name": "Lisa", "age": 27}, {"name": "Claire", "age": 28}]
group_obj2 = groupby(persons, key=lambda x: x["age"])   # Groups by which are same age
for key, value in group_obj2:   # Outputs   25 [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}]
    print(key, list(value))     #           27 [{'name': 'Lisa', 'age': 27}]    28 [{'name': 'Claire', 'age': 28}]

# Infinite operators
#   count
for i in count(10):         # Counts up by 1 from 10, without the if it would count forever
    print(i)
    if i == 15:
        break
#   cycle
list8 = [1, 2, 3]
for i in cycle(list8):      # This infinitely cycles through list8 until stop condition is made
    print(i)                # Outputs   1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 and so on
#   repeat
for i in repeat(1, 100):         # Makes an infinite loop of just 1s until it has done it 100 times
    print(i)
