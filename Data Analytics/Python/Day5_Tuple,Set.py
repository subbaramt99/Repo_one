My_tuple = (1, "python1", "3", 3, 5, "python", 7, 8, 9.10) # it is tuple ()
My_list = [1, 2, 3, 4, 5, "python", 7, 8, 9.10] # it is list []
#tuple[5] = "java"
My_list[5] = "java"
print(My_tuple)
print(My_list)
Converted_tuple = tuple(My_list)  # Type cast the list into tuple
print(Converted_tuple)
print(My_list)
#Converted_tuple[5] = "Hello"

print(My_tuple.count(3))  # it will return occurrence of the item
print(My_tuple.index("python")) # it will return the indexof value

for item in My_tuple:
    print(item)

#*************************************  Set  ************************************
My_set = {1, 2, 4, 5, "python", 9, 10.12, 5, 2} # It will not allow duplicate
converted_set = set(My_tuple)

print(converted_set)

My_set.add("Mukesh")
My_set.add("Mukesh")
My_set.remove(2)
print(My_set)

# ****************************** Dictionaries ****************************************
My_dic = {"name": "Mukesh", "age":26, "city": "chennai"}
print(My_dic["age"]) # Accessing value using key
print(My_dic.get("name")) # getting the value of key

My_dic["salary"] = 30000
print(My_dic)
