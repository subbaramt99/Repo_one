class Person:
    def __int__(self, name):
        self.name = name
    def say_hello (self):
        print("Hello {}!".format(self.name))

subbu = Person('SUBBARAM')
subbu.say_hello()