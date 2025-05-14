from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self) -> None:
        pass
    @abstractmethod
    def eat(self) -> None:
        pass

class Dog(Animal):
    def speak(self) -> None:
        print(type(self), ":  Woof!")
    def eat(self) -> None:
        print(type(self), ": Meat")

class Cat(Animal):
    def speak(self) -> None:
        print(type(self), ":  Meow!")
    def eat(self) -> None:
        print(type(self), ": Meat")

def animal_sound(animal: Animal) -> None:
    animal.speak()
def animal_eat(animal: Animal) -> None:
    animal.eat()

dog = Dog()
cat = Cat()
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
animal_eat(dog)  # Output: Meat
animal_eat(cat)  # Output: Meat