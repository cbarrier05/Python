import random
rand = int(input("How many elements in list to be sorted: "))
a = []
for i in range(0, rand):
    a.append(random.randint(0,10000))
n = len(a)
print("This is the starting list: ",a)
while n > 0:
    for count in range(0, n - 1):
        if a[count] > a[count+1]:
            temp = a[count]
            a[count] = a[count+1]
            a[count+1] = temp
    n -= 1
print("This is the sorted list: ",a)