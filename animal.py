# Dharyl Duclisen
# BSIT - 2

class Animal:
    def makesound(self):
        print("Says nothing")

class Dog(Animal):
    def makesound(self):
        print("Dog says \"woof\"")

class Cat(Animal):
    def makesound(self):
        print("Cat says \"meow\"")

animal = Animal()
animal.makesound()

dog = Dog()
dog.makesound()

cat = Cat()
cat.makesound()