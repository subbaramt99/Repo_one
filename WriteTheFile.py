# Read the file and store it in a list
# Reverse the list
# write the list in the file

# file = open("test.txt")
#
# file.close
with open("test.txt", 'r') as fileReader:  # open the file with read mode and this file will close once it done
    lst = fileReader.readlines()  # lst = [apple, ball, cat, dog, elephant, frog]
    rvsLst = reversed(lst)
    # print(rvsLst)
    #with open("test.xlsx", 'w') as fileWriter:

    with open("test.txt", 'w') as fileWriter:  # open the file with write mode
         for line in rvsLst:
             fileWriter.write(line)
