# Author Subbaram

import platform


def author():
    print('Hello world')
    print('I am SUBBARAM')


def platformversion():
    version = platform.python_version()
    print('The version of this platform is {}'.format(version))


def oprations():
    x = 5
    y = 3
    print('value of x and y is {}'.format(x + y))


def greateMe(name):
    print("Good morning " + name)


def addinteger(a, b):
    return a+b


author()
platformversion()
oprations()
greateMe("SUBBARAM")
print(addinteger(2, 5))
