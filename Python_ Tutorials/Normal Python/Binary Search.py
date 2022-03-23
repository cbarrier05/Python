import math

array = [0,1,2,4,3,5,6,7,8,9,10]
value = 3

def print_value(value, mid):
    print(value, "in position", mid)


def binarySearch(list1, value, temp, end):
    if value in temp:
        mid = round(len(list1)/2)
        if list1[mid] == value:
            print_value(value, temp.index(value))
        elif list1[mid] > value:
            list1 = list1[:mid]
            return binarySearch(list1, value, temp, end)
        else:
            list1 = list1[(mid -1):]
            return binarySearch(list1, value, temp, end)
    else:
        print(value,"not in list")


binarySearch(array, value, array, False)