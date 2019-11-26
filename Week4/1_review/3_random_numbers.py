from random import randint
from random import random
# This will print a random number between 0 and 1
print(random())
print(random())
# We can multiply the number by 100 to get a percentage
print(random() * 100)

# randint might be more useful. It prints a random number between the first number and the last number you pass in
print(randint(0, 1))
print(randint(0, 100))