
from abc import ABC, abstractmethod
import math

class Person:
    def __init__(self):
        self._age = 0
    def set_age(self, age):
        if age >= 0:
            self._age=age
        else:
            print("Возраст не может быть отрицательным")
    def get_age(self):
        return self._age

    class Animal
        def __init__(self, name):
            self.name = name
        def speak(self):
            return  "i am amimal"


    class Dog(Animal)
        def  speak(self):
            "Woof"

    class Cat(Animal)
        def speak(self):
            "Meow"


    class Vehicle
        def move(self):
            return "Vehicle is moving"


    class Car(Vehicle):
            def move(self):
                return "Car is driving"

    class Bicycle(Vehicle):
        def move(self):
            return vehicle.move()






