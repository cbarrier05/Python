import random       # Creates pseudo-random numbers as they seem random but are reproducible
import secrets      # Creates true random numbers

# import random
# Don't use for security as reproducible
a = random.random()         # produces random float between 0 and 1
b = random.uniform(1, 10)   # produces random float between 1 and 10
c = random.randint(1, 10)   # produces random integer between 1 and 10, including 10
d = random.randrange(1, 10)     # produces random integer between 1 and 10, not including 10
e = random.normalvariate(0, 1)  # produces random float within normal distribution with mean = 0,standard deviation = 1
list1 = list("ABCDEFGH")
f = random.choice(list1)    # Picks random element from list
g = random.sample(list1, 3)     # Produces random sample of 3 elements from list1, elements can only be picked once
h = random.choices(list1, k=3)  # Produces random sample of 3 elements from list1, elements can be picked multiple times
random.shuffle(list1)       # Shuffles list1 randomly and overwrites it into list1
# How to reproduce random numbers
random.seed(1)
i = random.randint(1, 10)
random.seed(1)
j = random.randint(1, 10)       # Both i and j have the same value despite using random

# import secrets
# Use for passwords and security tokens as not reproducible
# However less efficient
k = secrets.randbelow(10)   # Produce random into between 0 - 10, not including 10
m = secrets.randbits(4)     # Produces random number in the range of 0 - 4 bits, so actually 0 - 15
list2 = list("ABCDEFGH")
n = secrets.choice(list2)   # Picks random element from list2
