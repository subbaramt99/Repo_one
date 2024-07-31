# Classes are user defined blueprint or prototype ex: calculator
# Operation sum, multiplication, division, subtraction.
# Classes it has method, variables, instance variable, constructor etc...
# self keyword is mandatory for calling variables name into method
# instance and class variable have whole different purpose
# constructor name should be __init__
# new keyword is not required when you create object
class Calculator:  # Class
    num = 100   # class variables

    def __init__(self, a, b):   # it will call automatically (Constructor)
        self.dummy = None
        self.firstNumber = a
        self.secondNumber = b
        print("First number is:", a)
        print("Second number is:", b)
        print("I am called automatically when object is created")
    print(num)
    def getdata(self, dummy):  # Method
        print("Method executed")
        print(dummy)
        self.dummy = None
        print(dummy, dummy)

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num

# Reversed of string
    def Reverse(self, name):
        print(len(name))
        Reversed = ""
        for i in name:
            Reversed = i + Reversed
            print(Reversed)
        return Reversed

# print duplicate of string
#     def FindDuplicate(self, str1, str2):
#         Lstr1 = len(str1)
#         Lstr2 = len(str2)
#         #str3 = "Analytics Vidhya"
#         str3 = ""
#         for i in str1:
#             print(i)
#             for j in str2:
#                 print(i, j)
#                 if str1[i] == str2[j]:
#                     duplicate = str1[i]
#         print(duplicate)

    def Repeat(x):
        size = len(x)
        repeated = ""
        for i in range(size):
            k = i + 1
            for j in range(k, size):
                print(i, j, k)
                if x[i] == x[j] and x[i] not in repeated:
                    repeated.append(x[i])
        return repeated


    # Driver Code

obj = Calculator(2, 1)  # syntax to create an object in python
obj.getdata(10)
print(obj.num)
print(obj.summation())
print(obj.Reverse("subbaram"))
#obj.FindDuplicate("subbaram theerthagiri", "rathinavel theerthagiri")
str1 = "subbaram theerthagiri"
print(str1.split(" "))  # split() function separates the given string by the defined delimiter, i.e., space(” “)
list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
#print(obj.Repeat(list1))

#OOPS = Person('SUBBARAM')
#OOPS.say_hello()

class person:
    def __int__(self, name):
        self.name = name
    def say_hello (self):
        print("Hello {}!".format(self.name))

subbu = person('subbaram')
subbu.say_hello()
