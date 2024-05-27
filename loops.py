# if else
a = 4
if a > 2:
    print("a is greater then two")
else:
    print("a is not greater then two")

print("*******************************************")

# for loops
b=[1, 2, 3, 4, 5, 6]
for i in b:   # for(i=0;i<=6;i++)
    print("I is", i)
    print("Multiples of I in two", i*2)

print("*******************************************")
# sum of first five natural number 1+2+3+4+5 = 15
sums = 0
for j in range(1, 6):   # for(i=1;i<=5;i++)
    sums = sums + j
print("Sum is", sums)

print("*******************************************")

for k in range(1, 10, 2):    # for(k=1;k<=10;i+2)
    print(k)

print("*******************************************")

for l in range(10):    # for(l=0;l<=10;i++)
    print(l)

print("*******************************************")
# While Loops

it = 7
while it > 1:
    if it == 4:
        it = it - 1
        continue
    if it == 2:
        break
    print(it)
    it = it-1
