class Animal:
    def eat(self):
        print("Animal is eating")

class Pet:
    def play(self):
        print("Pet is playing")

class Dog(Animal, Pet):
    def bark(self):
        print("Dog is barking")

class Cat(Animal, Pet):
    def meow(self):
        print("Cat is meowing")

class Lab(Dog):
    def fetch(self):
        print("Labrador is fetching")

# Creating objects of Dog, Cat, and Lab classes
dog = Dog()
cat = Cat()
lab = Lab()

# Accessing methods from their respective classes
dog.eat()   
dog.play()  
dog.bark()  

cat.eat()  
cat.play()  
cat.meow()  

lab.eat()   
lab.play()  
lab.bark()  
lab.fetch() 
