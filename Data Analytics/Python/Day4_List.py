# List in python
list =[] # empty list
num = 10 # Integer data type
sting = "mukesh" # String
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # integer array
mixed_list = [1, "hello", 3.5, True] # List
'''
print("Data type of numbers is", type(numbers))
print(numbers[9])
print("Data type of mixed_list is", type(mixed_list))
print("Slicing list:", numbers[2:9])
Sliced_list = numbers[2:9]
print(Sliced_list[5])
Sliced_list[3] = "Hello" # Adding a value in index 6
print(Sliced_list)
print("Last index is ", Sliced_list[6])

# List methods
numbers.append(11) # Adding the index at last using append
#numbers.append("Hello")

print(numbers)
print(numbers[-1])
print(numbers[3])
numbers.insert(3, 100) # using insert
print(numbers[3])

numbers.remove(4) # It will remove the value
print(numbers)
numbers.pop(10)  # Remove the last index
print(numbers)

numbers.sort() # Sorting the list
print("Sorted list", numbers)'''

# find the even number in integer list
# sum of all the value of integer list
# Creating a mixed list and use the methods

for index in mixed_list:  # index is iterating variable through mixed_list one by one,
    print(index)  # mixed_list[index]

for i, v in enumerate(mixed_list):
    print(i, "is", v)
    #print(v)

print(10%2)  # it will return the reminder
print(10/2)   # it will return the quotient
print(15//2)  # integer divison
for i in range(10):
    if(i%2 == 0):   # i power of 2
        list.append(i)
print(list)

# List comperhension [expression for item in iterable]
lis = [i**2 for i in range(10)]
print(lis)