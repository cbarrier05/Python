# Q1
#x = int(input("Enter x: "))
#y = int(input("Enter y: "))
#
#z = x
#
#if x == y:
#    x *= x
#    y = (x+y)/2
#elif x < y:
#    y *= y
#    z = y-x
#    y = 200
#elif x > 0:
#    z = x / y
#    y = 200
#print("X:",x," Y:",y," Z:",z)


# Q2
#x = 5
#k = 10
#sum = 45
#while sum < 75:
#    sum += k
#    print("K:",k)
#    k += x
#print("Sum:",sum)


#3
#y = 2
#z = 1
#x = int(input("Enter positive integer:  "))
#while z != 0:
#    z = x % y
#    if z != 0:
#        y += 1
#if x == y:
#    print(x,"is in category 1")
#else:
#    print(x,"is in category 2")


# Q4
#temp = []
#day_avg = []
#day_max= 0
#while day_max != 999:
#    try:
#        day_max = float(input("Enter the maximum temp for day:  "))
#        if day_max != 999:
#            day_min = float(input("Enter the minimum temp for day:   "))
#            temp.append(day_min)
#            temp.append(day_max)
#            day_avg.append((day_max + day_min) / 2)
#    except ValueError:
#        print("A number must be given")
#total = 0
#for i in temp:
#    total += i
#average = total / (len(temp))
#above_avg = 0
#for y in day_avg:
#    if y > average:
#        above_avg += 1
#print(above_avg,"days above average")


# Q1
#for x in range(1,5):
#    country = "United States"
#    num = int(input("Enter a number:  "))
#    letter = country[num]
#    print(country[x] + letter)


# Q2
#for x in range (1,5):
#     num = int(input("Enter a number"))
#     operator = input("Enter operator")
#     if operator == "%":
#          print(num % x)
#     else:
#           print(num*x)


# Q3
