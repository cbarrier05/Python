import random
import time


def listCreation():
    randrange = int(input("Enter the possible range of random values:  "))
    rand = int(input("Enter the number of elements in the list (Must be >= range of values): "))
    list1 = random.sample(range(0, randrange), rand)
    list2 = list(list1)
    list3 = list(list1)
    return list1, list2, list3


def bubble(list1):
    start = time.time()
    n = len(list1)
    print("This is the starting list: ",list1)
    while n > 0:
        for count in range(0, n - 1):
            if list1[count] > list1[count + 1]:
                list1[count], list1[count + 1] = list1[count + 1], list1[count]
        n -= 1
    end = time.time()
    print("This is the sorted list: ",list1)
    print("It took ", end - start)


def merge(list3):



def insertion(list2):
    start2 = time.time()
    for i in range(1, len(list2)):
        item = list2[i]                                  # Sets item for comparison
        previous = i-1                                   # Finds the index of item lower than current
        while previous >= 0 and list2[previous] > item:  # Compares item with one lower
            list2[previous + 1] = list2[previous]        # Moves previous up so that there is space for the insertion
            previous -= 1                                # Moves down the list until reaches end
        list2[previous + 1] = item                       # Once reaches end or finds position it inserts it
    end2 = time.time()
    print("This is the sorted list: ", list2)
    print("It took: ", end2 - start2)


list1, list2, list3 = listCreation()
#bubble(list1)
#insertion(list2)