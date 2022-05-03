

'''
Python 3.10.0
Purpose: demonstrate inheritance by creating two classes that
inherit from a third class
'''

#create initial class and assign 3 attributes
class Vehicle:
    wheels = 4
    make = ''
    model = ''

    #create a method for the initial class
    def Accelerate(self):
        print("This vehicle can move forward.")

#create class that inherits from initial class and assign 2 attributes
class Car(Vehicle):
    doorNum = 4
    sunRoof = True

    #use polymorphism to override the inherited class method
    def Accelerate(self):
        print("This car can move forward.")

#create another class that inherits from initial class and assign 2 attributes
class Truck(Vehicle):
    extCab = True
    diesel = False

    #use polymorphism to override the inherited class method
    def Accelerate(self):
        print("This truck can move forward.")

