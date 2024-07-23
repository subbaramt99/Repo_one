import sys
import platform
import datetime

print(" pyhton version")
print(sys.version)
print(platform.version())

## printing current date and time ##

now = datetime.datetime.now()
print(now)

## Calculating the area of the circle ##

print("Enter radius of the circle:")
radius = float(input())
area = (3.144 * radius * radius)
print("Area of the circle:", area)

## Write a program to print the given number is odd or even.

print("Enter the number: ")
num = int(input())
if num%2 == 0:
    print("{0} is EVEN".format(num))
else:
    print("{0} is ODD".format(num))


