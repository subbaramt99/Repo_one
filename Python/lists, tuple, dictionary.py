values = [1, 2, "ram", 3, 4]
print(values[1])  # 2
print(values[2])  # ram
print(values[-1])  # 4
values.insert(3, "nivi")
print(values)  # [1, 2, ram, nivi, 3, 4]
print(values[1:4])  # [2, ram, nivi]
values.append("end")
print(values)  # [1, 2, ram, nivi, 3, 4, end]
values[2] = "RAM"
print(values)
del values[1] # [1, 'RAM', 'nivi', 3, 4, 'end']
print(values)


# Tuple - same as LIST data type but it is immutable.
# TypeError: 'tuple' object does not support item assignment
val = (2, 3, "ram", 4)
print(val[1]) # 3
# val[2] = "RAM"
print(val) # (2, 3, 'ram', 4)

# Dictionary - in java it is call it as a Ash mapping
# print value having key = 1
dictionary = {1:"subbarm", 2:"ram", 3:"surya", "a":5, "c":"hello"}
print(dictionary) # {1: 'subbarm', 2: 'ram', 3: 'surya', 'a': 5, 'c': 'hello'}
print(dictionary[1]) # subbarm
print(dictionary["a"]) # 5
print(dictionary["c"]) # hello

dic = {}
dic["1st name"] = "subbaram"
dic["last name"] = "theerthagiri"
dic[3] = 23
print (dic)