file = open("test.txt")
# file.read()  # Read all the content of file
# print(file.read())  # Read and print all the content of file
# print(file.read(10))  # Read and print only 10 indices of the content of file
# print(file.readline())  # Read one single line at a time readline
line = file.readline()  # Read one single line
while line != "": # Read the content and print it line by line using readline method
    print(line)
    line = file.readline()

# values = [apple, ball, cat, dog, elephant, frog]
for line in file.readlines():  # Readlines it takes as a list and iterate one by one index
    print(line)



file.close()

