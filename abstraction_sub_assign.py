
'''
Python 3.10.0
Purpose: demonstrate abstraction by creating a child class that implements
    an abstract method from it's parent.
'''
#import the abstract base class
from abc import ABC, abstractmethod

#create the goodest of boys class that inherits from ABC
class Dog(ABC):
    #create an abstract method
    def speak(self, sound):
        print("{}".format(sound))
        
    @abstractmethod
    def howl(self, sound):
        pass

    #create a regular method
    def rollOver(self):
        print("The dog rolls over.")

#create child class that implements the abstract method from parent
class Corgi(Dog):
    def howl(self, sound):
        print("{}-Awoooo!".format(sound))

#give our good boy a name (create obj)
Spot = Corgi()

#call parent and child methods
Spot.speak('Ruff')
Spot.howl('Aow-Aow')
Spot.rollOver()
