
'''
Python 3.10.0
Purpose: create a class with a private and a protected attribute. instantiate an
    object that makes use of both.
'''

#create the goodest of boys class
class Dog:
    def __init__(self):
        #protected
        self._bark = 'Ruff'
        #private
        self.__howl = 'Awoo'

    def printHowl(self):
        print(self.__howl)

#give our good boy a name (create obj)
Spot = Dog()

#ask our good boy to speak (use the protected attrib)
print(Spot._bark)

#ask Spot to sing (use private attrib thru a fn)
Spot.printHowl()
