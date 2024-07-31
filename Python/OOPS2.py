# A class is a collection of objects.
# A class contains the blueprints or the prototype from which the objects are being created.
# It is a logical entity that contains some attributes and methods
class Pump:
    def __init__(self):
        print("init")

    def getPumps(self):
        pass

p = Pump.getPumps('hello')
print(p)


class dog:
    pass
    def __int__(self):
        print("Welcome to dogs world")

    def getName(self,name):
        print(name)

obj = dog()  # Object
dog.getName('labrador')
