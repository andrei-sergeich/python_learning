# Задание 1
# Задан словарь. Напишите программу, 
# которая будет выводить значение по заданному ключу.
print("Задание 1. Вариант решения №1")

# d = dict(Hello = 'Hi', Bye = 'Goodbye', List = 'Array')
# print(d)

dct = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}
key = input("Введите ключ: ")

for i in dct.keys():
    if i == key:
        print(dct[i])


print()
print("Задание 1. Вариант решения №2")

dct = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}
key = input("Введите ключ: ")

print(dct.get(key))


print()
print("----------------------------")
print()

# Задание 2
# Напишите программу, которая будет выполнять действие, обратное заданию 1. 
# Программа должна производить поиск по значению и выдавать ключ.
print("Задание 2. Вариант решения № 1")

my_dict = {'Hello' : 'Hi', 'Bye' : 'Goodbye', 'List' : 'Array'}
my_value = input("Введите значение: ")

for key, value in my_dict.items():
    if value == my_value:
        print(key)


print()
print("Задание 2. Вариант решения № 2")

my_dict = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}
my_value = int(input("Введите значение: "))

for key in my_dict:
    if my_dict[key] == my_value:
        print(key)


print()
print("Задание 2. Вариант решения № 3")

my_dict = {'Hello' : 'Hi', 'Bye' : 'Goodbye', 'List' : 'Array'}
my_value = input("Введите значение: ")
rev_dict = dict((v, k) for k, v in my_dict.items())

for key in my_dict:
    if my_dict[key] == my_value:
        print(key)


print()
print("----------------------------")
print()

# Задание 3
# Напишите программу, которая принимает список строк и 
# выводит количество повторений данных строк в списке.
print("Задание 3. Вариант решения № 1")

str_lst = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
my_dict = dict.fromkeys(str_lst, 0)

it = 0
while it < len(str_lst):
    for key in my_dict.keys():
        if key == str_lst[it]:
            my_dict[key] += 1
    it += 1

print(*my_dict.values())


print()
print("Задание 3. Вариант решения № 2")

str_lst = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
my_dict = {i: str_lst.count(i) for i in str_lst}

print(*my_dict.values())


print()
print("Задание 3. Вариант решения № 3")

str_lst = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']

my_dict = dict.fromkeys(str_lst, 0)

for it in str_lst:
    my_dict[it] += 1

print(*my_dict.values())
