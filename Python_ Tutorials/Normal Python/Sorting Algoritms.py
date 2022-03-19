import random
import time


def listCreation():
    randrange = int(input("Enter the possible range of random values:  "))
    rand = int(input("Enter the number of elements in the list (Must be <= range of values): "))
    list1 = random.sample(range(0, randrange), rand)
    list2 = list(list1)
    list3 = list(list1)
    print("This is the starting list: ", list1)
    return list1, list2, list3, rand


def bubble(list1):
    start = time.time()
    n = len(list1)
    while n > 0:
        for count in range(0, n - 1):
            if list1[count] > list1[count + 1]:
                list1[count], list1[count + 1] = list1[count + 1], list1[count]
        n -= 1
    end = time.time()
    print("This is the sorted list: ",list1)
    print("It took ", end - start)


def insertion(list2):
    start = time.time()
    for i in range(1, len(list2)):
        item = list2[i]                                  # Sets item for comparison
        previous = i-1                                   # Finds the index of item lower than current
        while previous >= 0 and list2[previous] > item:  # Compares item with one lower
            list2[previous + 1] = list2[previous]        # Moves previous up so that there is space for the insertion
            previous -= 1                                # Moves down the list until reaches end
        list2[previous + 1] = item                       # Once reaches end or finds position it inserts it
    end = time.time()
    print("This is the sorted list: ", list2)
    print("It took: ", end - start)


def mergeSort(list3):
    if len(list3) > 1:
        # Finding the mid of the array
        mid = len(list3) // 2
        # Dividing the array elements
        left = list3[:mid]
        # into 2 halves
        right = list3[mid:]
        # Sorting the first half
        mergeSort(left)
        # Sorting the second half
        mergeSort(left)
        a, b, c = 0, 0, 0
        # Copy data to temp arrays left and right
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list3[c] = left[a]
                a += 1
            else:
                list3[c] = right[b]
                b += 1
            c += 1
        # Checking if any element is left over
        while a < len(left):
            list3[c] = left[a]
            a += 1
            c += 1
        while b < len(right):
            list3[c] = right[b]
            b += 1
            c += 1


def merge(list3):
    start = time.time()
    mergeSort(list3)
    end = time.time()
    print("This is the sorted list: ", list2)
    print("It took: ", end - start)


list1, list2, list3, rand = listCreation()
bubble(list1)
insertion(list2)
merge(list3)