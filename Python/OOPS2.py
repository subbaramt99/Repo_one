# A class is a collection of objects.
# A class contains the blueprints or the prototype from which the objects are being created.
# It is a logical entity that contains some attributes and methods
class Pump:

    company = 'crompton'
    def __init__(self):
        print("init")

    def getPumps(self):
        pass

p = Pump.getPumps("hello")
q = Pump()
print(p)
print("Name of the Company is: {}".format(q.__class__.company))


class Dog:

    # class attribute
    attr1 = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name

# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))

