numbers = [1,2,3,4,5,6,7,8,9]

list_of_squared_numbers = []
for number in numbers:
    squared_number = number * number
    list_of_squared_numbers.append(squared_number)

print(list_of_squared_numbers)

def square(x):
    return x*x

list_of_squared_numbers2 = list(map(square, numbers))
print(list_of_squared_numbers2)

def power_of(x, y):
    return x ** y

#2 arguments
new_list = list(map(power_of, numbers, len(numbers)*[2]))
print(new_list)

#using anonymous function
squared_numbers = list(map(lambda x: x*x, numbers))
print(squared_numbers)

print(list(map(lambda x: x**6, numbers)))

print(list(map(lambda x: x%2 == 0, numbers)))

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

summed_lists = list(map(lambda x, y: x+y, list1, list2))
print(summed_lists)


#with strings
names = ['alice', 'bob', 'charles']

names2 = []
for name in names:
    names2.append(name.capitalize())
print(names2)

#using map
names2 = list(map(str.capitalize, names))
print(names2)
