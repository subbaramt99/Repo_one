def add(a, b, c):
    return a+b+c
add(10,20, 30)

def square(x):
    return x*x

add = lambda a,b,c: a+b+c
print(add(20,30,40))

# square using lambda function

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14] # list

#Syntax map(expression: iterables)
squared_list = list(map(lambda x: x*x, numbers))
print(squared_list)

def get_name(person):
    return person['salary']

people =[{'name': 'jack', 'age': 26, 'salary': '100000'}, {'name': 'jelly', 'age': 24, 'salary': '200000'}]
#print(people[0])

list_name = list(map(get_name, people))
print(list_name)

def odd(num):
    if(num%2 == 1):
        return True
#even(15)
#print(even(10))

print(list(filter(odd, numbers)))

even_number = list(filter(lambda num:num%2==0, numbers))
print(even_number)

