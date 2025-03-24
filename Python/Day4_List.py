# List in python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # integer array
mixed_list = [1, "hello", 3.5, True] # List

print(type(numbers))
print(numbers[-1])
print(type(mixed_list))
print("Slicing list:", numbers[2:9])
Sliced_list = numbers[2:9]
#print(Sliced_list[7])
Sliced_list[6] = "Hello"
print("Last index is ", Sliced_list[6])

# List methods
numbers.append(11) # Adding tthe index at last using append
numbers.append(12)
print(numbers)
print(numbers[-1])
print(numbers[3])
numbers.insert(3, 100) # using insert
print(numbers[3])

numbers.remove(3) # It will remove the value
print(numbers)
numbers.pop(10)  # Remove the last index
print(numbers)

numbers.sort() # Sorting the list
print("Sorted list", numbers)

# find the even number in integer list
# sum of all the value of integer list
# Creating a mixed list and use the methods
