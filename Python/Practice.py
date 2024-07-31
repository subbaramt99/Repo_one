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

def Area_of_circle():
    print("Enter radius of the circle:")
    radius = float(input())
    area = (3.144 * radius * radius)
    print("Area of the circle:", area)

## Write a program to print the given number is odd or even.
def Odd_or_Even():
    print("Enter the number: ")
    num = int(input())
    if num%2 == 0:
        print("{0} is EVEN".format(num))
    else:
        print("{0} is ODD".format(num))

# Write a program to find the given number is positive or negative.
#print("Enter the number: ")
def Pov_or_Nev():
    num1 = float(input("Enter the number: "))
    if num1 == 0:
        print("{0} the given number is Zero".format(num1))
    elif num1 >= 1:
        print("{0} the given number is Positive".format(num1))
    else:
        print("{0} the given number is Negative".format(num1))

# Write a program to find if the given number is prime or not.
def prime():
    num = int(input("Enter the number: "))
    flag = False
    if num > 1:
        for i in range(2, num):
            if num%i == 0:
                print("Number is divisible by ",i)
                flag = True
                break
    if flag:
        print("{0} the given number is not a prime".format(num))
    else:
        print("{0} the given number is a prime".format(num))

# Write a program to check if the given number is palindrome or not
def palindrome():
    num = int(input("Enter a number: "))
    temp = num
    reverse = 0
    while temp >= 1: # 657756
        remainder = temp%10
        reverse = (reverse * 10) + remainder
        temp = temp//10
    print(reverse)
    if num == reverse:
        print("Given number is palindrome")
    else:
        print("Given number is not a palindrome")

# Write a program to check if the given number is Armstrong or not.
def Armstrong():
    num = int(input("Enter a number: "))
    temp = num
    sum = 0
    while temp >= 1:
        rem = temp%10
        cube = rem * rem * rem
        sum = sum + cube
        cube = 0
        temp = temp//10
    if num == sum:
        print("Given number is Armstrong number")
    else:
        print("Given number is not Armstrong number")

# Write a program to check if the given strings are anagram or not.
def Anagram():
    s1 = str(input("Enter string 1:"))
    s2 = str(input("Enter string 2:"))
    if sorted(s1) == sorted(s2):
        print("The string is anagram")
    else:
        print("The string is not a anagram")

# Write a program to find a factorial of a number.
def Factorial():
    num = int(input("Enter a number: "))
    fac = 1
    for i in range (1, num+1):
        fac = fac * i
    print("Factorial of {0} is: ".format(num), fac)

# Write a program to find a fibonacci of a number.
def fibonacci_num():
    nth = int(input("Enter a nth number: "))
    n1 = 0
    n2 = 1
    fib = 0
    if nth > 1:
        print(n1)
        print(n2)
        for i in range (1, nth-1):
            nth = n1 + n2
            n1 = n2
            n2 = nth
            print(nth)

    elif nth == 1:
        print("Fibonacci sequence upto", nth, ":")
        print(n1)
    else:
        print("Please enter valid nth number")









#Area_of_circle()
#Odd_or_Even()
#Pov_or_Nev()
#prime()
#palindrome()
#Armstrong()
#Anagram()
#Factorial()
#fibonacci_num()