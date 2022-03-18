import random
import time
rand = int(input("How many elements in list to be sorted: "))
a = random.sample(range(0, 10000), rand)
start = time.time()
for i in range(1, len(a)):
    item = a[i] # Sets item for comparison
    previous = i-1  # Finds the index of item lower than current
    while previous >= 0 and a[previous] > item: # Compares item with one lower
        a[previous + 1] = a[previous] # Moves everything up giving room for item when it is inserted
        previous -= 1   # Moves down the list until reaches end
    a[previous + 1] = item  # Once reaches end or finds position it inserts it
end = time.time()
print("This is the sorted list: "a)
print("It took: ", end-start)