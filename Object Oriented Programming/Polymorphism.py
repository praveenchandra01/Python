class Animal:
    def __init__(self,name):
        self.name=name
    def talk(self):
        raise NotImplementedError("Derived class must implement this function")
class Cat(Animal):
    def talk (self):
        return "meow"
class Dog(Animal):
    def talk(self):
         return "bhao"
animals=[Cat("Rekha"),Cat("Madhuri"),Dog("Vinod"),Cat("Rupa")]

for animal in animals:
    print(animal.name," - ",animal.talk())
