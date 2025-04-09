#for variable in sequence:  --> Syntex
start = 7 # Variable
stop = 10
for i in range(start, stop):
    print(i)

for char in "python":
    print(char)

fruits = ["apple", "bannana", "cherry", "orange"]
for fruit in fruits:
    print(fruit == "bannana")

#while condition: --> syntex
i = 1
while i <= 10:
    if i == 5:
        break
        #continue
    print(i)
    i += 1 #--> i = i + 1

#Sum of n natural numbers
num = int(input("Enter a Natural number: "))
summ = 0
j = 1
while j <= num:
    summ = summ + j
    #print("Sum ", summ)
    j += 1
    #print("j is", j)
print(f"Sum of {num} natural number is: ", summ)
