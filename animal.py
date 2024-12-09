# Name: Dharyl Duclisen
# Course: BSIT - 2
# Filename: person.py

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
