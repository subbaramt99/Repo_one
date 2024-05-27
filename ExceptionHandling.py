class ItemInCart:
    pass

ItemInCart == 0  # 2 item will be added in cart

if ItemInCart != 2:
    pass
#    raise Exception ("Products count is not matching")

#assert (ItemInCart == 0)

# try, catch

try:
    with open("test.txt", 'r') as reader:
        reader.read()
        print("test file read successfully")
except:
    print("test file is not exist")

try:
    with open("test32.txt", 'r') as reader:
        reader.read()
        print("test32 file opened successfully")
except:
    print("test32 file is not exist")  # it will through the customized error message

try:
    with open("test32.txt", 'r') as reader:
        reader.read()
        print("test32 file opened successfully")
except Exception as e:
    print(e)   # it will through the actual error message of python
finally:
    print("cleaning resources")  # irrespective of error in try or except finally will execute




