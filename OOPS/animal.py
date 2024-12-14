class Animal:
    def eat(self):
        print("Animal is eating")
class Mammal(Animal):
    def walk(self):
        print("Animal is walking")
class Dog(Mammal):
    def bark(self):
        print("Dog is barking")
dog=Dog()
dog.eat()
dog.walk()
dog.bark()