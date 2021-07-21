# Задание 1
# Напишите программу, которая принимает арифметическое выражение
# в качестве аргумента и выводит результат этого выражения.
# Программа должна поддерживать следующие арифметические операции:
# +, -, /, *, %(получение процента от числа),
# **(возведение в квадрат),
# **х(возведение в степень числа х).
# Запрещено подключать дополнительные модули.
# Для вывода результата необходимо использовать функцию print().
print("Задание 1. Вариант решения №1")


def expression(x, s, y):
    ''' Функция expression(c) принимает
        арифметическое выражение в качестве
        аргумента и выводит результат этого выражения
    '''
    if s in ('+', '-', '*', '/', '**', '%'):
        if s == '+':
            return x + y
        elif s == '-':
            return x - y
        elif s == '-':
            return x - y
        elif s == '*':
            return x * y
        elif s == '/':
            return x / y
        elif s == '**':
            if y:
                return x ** y
            else:
                return x ** 2
        elif s == '%':
            if y:
                return x * y / 100
            else:
                return x * 1 / 100
    else:
        return "Неверный знак операции"


x = int(input("x = "))
s = input("Операция (+,-,*,/,**,%): ")
y = int(input("y = "))

print(expression(x, s, y))


print()
print("Задание 1. Вариант решения № 2")


def parsing(exp_str):
    ''' Функция parsing(exp_str) принимает
        арифметическое выражение в качестве
        аргумента, находит в нем числа и
        математическое действие, которое
        необходимо выполнить с этими числами
        и возвращает список из 2-х либо 3-х элементов
    '''
    id = 0
    x = ''
    action = ''
    y = ''

    while exp_str[id].isdigit():
        x += exp_str[id]
        id += 1
    if exp_str[id] == '+':
        action += exp_str[id]
        id += 1
    elif exp_str[id] == '-':
        action += exp_str[id]
        id += 1
    elif exp_str[id] == '-':
        action += exp_str[id]
        id += 1
    elif exp_str[id] == '/':
        action += exp_str[id]
        id += 1
    elif exp_str[id] == '%':
        action += exp_str[id]
        id += 1
    elif exp_str[id] == '*':
        if id + 1 < len(exp_str) and exp_str[id + 1] == '*':
            action += exp_str[id] + exp_str[id + 1]
            id += 2
        else:
            action += exp_str[id]
            id += 1
    else:
        return "Неверный знак операции"
    while id < len(exp_str) and exp_str[id].isdigit():
        y += exp_str[id]
        id += 1
    x = int(x)
    if len(y) > 0:
        y = int(y)
        return [x, action, y]
    else:
        return [x, action]


def calculating(expression):
    ''' Функция calculating(expression)
        принимает список в качестве аргумента,
        и выполняет математическое действие,
        возвращает результат вычислений
    '''
    x = expression[0]
    action = expression[1]

    if len(expression) == 3:
        y = expression[2]
        if action == '+':
            return x + y
        elif action == '-':
            return x - y
        elif action == '/':
            return x / y
        elif action == '*':
            return x * y
        elif action == '**':
            return x ** y
        elif action == '%':
            return (x * y) / 100
    else:
        if action == '**':
            return x ** 2
        elif action == '%':
            return x / 100


exp_str = input("Введите выражение: ")
expression = parsing(exp_str)
if type(expression) is not str:
    result = calculating(expression)
    print(result)
else:
    print(expression)


print()
print("Задание 1. Вариант решения № 3")


def calculating(x, action, y=None):
    ''' Функция calculating(x, action, y=None)
        принимает список в качестве аргумента,
        и выполняет математическое действие,
        возвращает результат вычислений
    '''

    if y:
        if action == '+':
            return x + y
        elif action == '-':
            return x - y
        elif action == '/':
            return x / y
        elif action == '*':
            return x * y
        elif action == '**':
            return x ** y
        elif action == '%':
            return (x * y) / 100
    else:
        if action == '**':
            return x ** 2
        elif action == '%':
            return x / 100


def parsing(expr_str):
    ''' Функция parsing(exp_str) принимает
        арифметическое выражение в качестве
        аргумента, находит в нем числа и
        математическое действие, которое
        необходимо выполнить с этими числами,
        вызывает функцию calculating(x, action, y=None)
        и возвращает результат работы функции calculating
    '''
    idx = 0
    x = ''
    action = ''
    y = ''

    while expr_str[idx].isdigit():
        x += expr_str[idx]
        idx += 1
    if expr_str[idx] == '+':
        action += expr_str[idx]
        idx += 1
    elif expr_str[idx] == '-':
        action += expr_str[idx]
        idx += 1
    elif expr_str[idx] == '-':
        action += expr_str[idx]
        idx += 1
    elif expr_str[idx] == '/':
        action += expr_str[idx]
        idx += 1
    elif expr_str[idx] == '%':
        action += expr_str[idx]
        idx += 1
    elif expr_str[idx] == '*':
        if idx + 1 < len(expr_str) and expr_str[idx + 1] == '*':
            action += expr_str[idx] + expr_str[idx + 1]
            idx += 2
        else:
            action += expr_str[idx]
            idx += 1
    else:
        return "Неверный знак операции"
    while idx < len(expr_str) and expr_str[idx].isdigit():
        y += expr_str[idx]
        idx += 1
    x = int(x)
    if len(y) > 0:
        y = int(y)
        res_of_calc = calculating(x, action, y)
    else:
        res_of_calc = calculating(x, action)
    return res_of_calc


exp_str = input("Введите выражение: ")
result = parsing(exp_str)
print(result)
