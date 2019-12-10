class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

class Warrior:
    def __init__(self, weapon, armor, hp):
        self.weapon = weapon
        self.armor = armor
        self.hp = hp

knight = Warrior("sword", "steel", 200)
mario = Warrior("fireballs", "plumber outfit", 50)