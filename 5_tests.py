# Задание 1
# Задан массив из 10 чисел. 
# Напишите программу, которая выводит их сумму.
array = [758, 483, 893, 393, 293, 292, 292, 485, 828, 182]
print(type(array))
total = 0
print(sum(array))
for number in array:
    total += number
print(total)

my_list = [758, 483, 893, 393, 293, 292, 292, 485, 828, 182]
i1 = 0
total2 = 0
while i1 < len(my_list):
    total2 += my_list[i1]
    i1 += 1
print(total2)

print()


# Задание 2
# Задан массив из n чисел. 
# Напишите программу, которая считает и выводит количество чисел равных нулю.
array = [700, 8, 89, 20, 13, 0]
total = 0
for number in array:
    if number == 0:
        total += 1
print(total)
print()


# Задание 3
# По данному натуральному n ≤ 9 выведите лесенку из n ступенек, 
# i-я ступенька состоит из чисел от 1 до i без пробелов.
var = 0
n = int(input('Введите данные '))
i = 1
while i <= n:
    var = var * 10 + i
    print(var)
    i += 1

var2 = 0
x = 5
for i in range(1, x + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

a = int(input('Введите данные '))
s = ""
for i in range (a):
    s = s + str(i + 1)
    print(s)

x = int(input('Введите данные '))
s = ''
for i in range(1, x + 1):
    s += str(i)
    print(s)

n = int(input('Введите данные '))
for i in range(1, n + 1):
    print(*range(1, i + 1), sep='')

print()


# Задание 4
# Дополните код из предыдущего задания, чтобы теперь получалась пирамида. 
# То есть каждая ступень состоит из чисел от 1 до i и обратно.
n = int(input('Введите данные '))
i = 1
j = n - 1
s = ''
while i <= n:
    s += str(i)
    print(' ' * (n - i), s, s[-2::-1], sep='')
    i += 1

n = int(input('Введите данные '))
for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    print(*range(1, i + 1), *range(1, i)[::-1], sep='')

x = int(input('Введите данные '))
s = ''
for i in range(1, x + 1):
    s += str(i)
    print(' ' * (x - i) + s + s[-2::-1])

print()


# Задание 5
# Дополните код из предыдущего задания, чтобы теперь получался ромб. 
# То есть количество ступеней должно равняться числу n*2-1.
i = 5
s = '12345'
while i > 0:
    s = s[:i]
    print(s[::-1])
    i -= 1

n = int(input('Введите данные '))
s = ''
i = 1
while i <= n:
    s += str(i)
    print(' ' * (n - i), end='')
    print(s, s[-2::-1], sep='')
    i += 1
i -= 2
while i > 0:
    s = s[:i]
    print(' ' * (n - i), end='')
    print(s[0:i], s[-2::-1], sep='')
    i -= 1

n = int(input('Введите данные '))
for i in range(1, n * 2 + 1):
    if i <= n:
        print(' ' * (n - i), end='')
        print(*range(1, i + 1), *range(1, i)[::-1], sep='')
    else:
        print(' ' * (i - n), end='')
        print(*range(1, n*2 - i + 1), *range(1, n*2 - i)[::-1], sep='')

print()


# Бонусное задание
# Используя циклы, напишите код, который бы выводил данную фигуру:
# Программа должна выводить фигуру разной величины, в зависимости от входного параметра. 
# Значение параметра может принимать значения от 0 до 9.
print('Бонусное задание')

# Вариант 1
print('Вариант 1')
n = int(input('Введите данные '))
s = ''
i = 1
while i <= n:
    s += str(i)
    print(' ' * (n - i), end='')
    print(s)
    i += 1
i -= 1
while i > 0:
    s = s[:i]
    print(' ' * (n), end='')
    print(s[::-1])
    i -= 1

n = int(input('Введите данные '))
for i in range(1, n * 2 + 1):
    if i <= n:
        print(' ' * (n - i), end='')
        print(*range(1, i + 1), sep='')
    else:
        print(' ' * (n), end='')
        print(*range(1, n*2 - i + 2)[::-1], sep='')

# Вариант 2
print('Вариант 2')
n = int(input('Введите данные '))
s = ''
i = 1
while i <= n:
    s += str(i)
    print(' ' * (n), end='')
    print(s[::-1])
    i += 1
i -= 1
while i > 0:
    s = s[:i]
    print(' ' * (n - i), end='')
    print(s)
    i -= 1

n = int(input('Введите данные '))
for i in range(1, n * 2 + 1):
    if i <= n:
        print(' ' * (n), end='')
        print(*range(1, i + 1)[::-1], sep='')
    else:
        print(' ' * (i - n - 1), end='')
        print(*range(1, n*2 - i + 2), sep='')

# Вариант 3
print('Вариант 3')
n = int(input('Введите данные '))
s = ''
i = 1
while i <= n:
    s += str(i)
    print(' ' * (n - i), end='')
    print(s)
    i += 1
i -= 2
while i > 0:
    s = s[:i]
    print(' ' * (n - i), end='')
    print(s[0:i])
    i -= 1

n = int(input('Введите данные '))
for i in range(1, n * 2 + 1):
    if i <= n:
        print(' ' * (n - i), end='')
        print(*range(1, i + 1), sep='')
    else:
        print(' ' * (i - n), end='')
        print(*range(1, n*2 - i + 1), sep='')

# Вариант 4
print('Вариант 4')
n = int(input('Введите данные '))
s = ''
i = 1
while i <= n:
    s += str(i)
    print(' ' * (n), end='')
    print(s[::-1])
    i += 1
i -= 2
while i > 0:
    s = s[:i]
    print(' ' * (n), end='')
    print(s[::-1])
    i -= 1

n = int(input('Введите данные '))
for i in range(1, n * 2 + 1):
    if i <= n:
        print(' ' * (n), end='')
        print(*range(1, i + 1)[::-1], sep='')
    else:
        print(' ' * (n), end='')
        print(*range(1, n*2 - i + 1)[::-1], sep='')
