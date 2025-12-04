# Hiding internal details and Showing only assential features.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    # When we do not implement any thing we write pass, It showas none.

class Lion(Animal):
    def make_sound(self):
        print("Roar")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

Lion = Lion()
Lion.make_sound()

Cat = Cat()
Cat.make_sound()


# Here we hide the implementation details.