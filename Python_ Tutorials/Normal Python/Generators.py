# Generator is much more efficient than lists
# Take up less memory

#def generator1():
#    yield 1
#    yield 2     # This generator contains 1, 2, 3
#    yield 3
#g = generator1()
#for i in g:      # Iterates through generator, printing each element
#    print(i)
#value = next(g)     # First element
#value2 = next(g)    # Second element
#sorted(g)       # returns sorted list with elements in order

#def countdown(num):
#    print("Starting")
#    while num > 0:
#        yield num
#        num -= 1
#cd = countdown(5)   # Doesn't output "Starting" until first outputted
#for i in cd:
#    print(i)

#def firstn(n):
#    num = 0
#    while num < n:
#        yield num
#        num +=1      # Adds all number from 0 to n to the generator
#for i in firstn(10):
#    print(i)            # Lists 0-9

# Generator expressions
generator = (i for i in range(10) if i % 2 == 0)  # Set to 0,2,4,6
