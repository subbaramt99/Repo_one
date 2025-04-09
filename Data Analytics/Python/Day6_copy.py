import copy
lis = [1,2,3,4,5,6,7]
original_list = [[1,2,3,4], [5,6,7,8], [9,10]]

shallow_copy_list = copy.copy(original_list)
print(shallow_copy_list[1])
print(lis[1])

shallow_copy_list[2][1] = 100
print('shallow copy ', shallow_copy_list)
print("original list:", original_list)

deep_copy_list = copy.deepcopy(original_list)
print(deep_copy_list)

shallow_copy_list[2][1] = 1000
print("Deep copy after chnages in shallow copy", deep_copy_list)
print('shallow copy ', shallow_copy_list)
print("Deep copy after chnages in shallow copy", deep_copy_list)
print(original_list)
deep_copy_list = copy.deepcopy(original_list)
print(deep_copy_list)

#************************************** Function in python **************************************

class My_main(): # it is a class it has methods and variables
    def __init__ (self):  # it will initiate when object of the class is called
        print("Hi muksh")
        My_main.My_method()

    def My_method(self):  # method or function
        print("helloworld")
a = My_main()  # a is an object of the My_main class
#My_main.My_method()