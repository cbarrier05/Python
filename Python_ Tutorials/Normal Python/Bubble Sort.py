import random
import time
rand = int(input("How many elements in list to be sorted: "))
a = random.sample(range(0,10000), rand)
b = list(a)
start = time.time()
n = len(a)
print("This is the starting list: ",a)
while n > 0:
    for count in range(0, n - 1):
        if a[count] > a[count+1]:
            temp = a[count]
            a[count] = a[count+1]
            a[count+1] = temp
    n -= 1
end = time.time()
print("This is the sorted list: ",a)
print("It took ", end - start)

start2 = time.time()
for i in range(1, len(b)):
    item = b[i] # Sets item for comparison
    previous = i-1  # Finds the index of item lower than current
    while previous >= 0 and b[previous] > item: # Compares item with one lower
        b[previous + 1] = b[previous] # Moves everything up giving room for item when it is inserted
        previous -= 1   # Moves down the list until reaches end
    b[previous + 1] = item  # Once reaches end or finds position it inserts it
end2 = time.time()
print("This is the sorted list: ", b)
print("It took: ", end2 - start2)