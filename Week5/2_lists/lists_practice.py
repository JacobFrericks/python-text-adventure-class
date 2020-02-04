# Lists provide a way to save a bunch of information in one variable

# Lists
# This is how you create a list of numbers
my_list = [1, 2, 3, 4]
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])

print("*******")

# You can change any part of the list you want
my_list[2] = 100
print(my_list)

print("*******")

# You can also have a list of strings!
my_list = ["this is cool", "AWESOME", "MARIO"]
print(my_list[1])

print("*******")

# In python you can have a list of both numbers and strings!
my_list = [1, "MARIO"]
print(my_list[0])

print("*******")

# Shorter way to create a list of ordered numbers
my_list = range(1, 4)
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])

# You can even have a list of objects!
class SomeObject:
    def __init__(self, damage):
        self.damage = damage
my_list = [SomeObject(20), SomeObject(40)]

