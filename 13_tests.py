# Задание 1
# Напишите программу, которая принимает арифметическое выражение 
# в качестве аргумента и выводит результат этого выражения.
print("Задание 1. Вариант решения №1")

def expression(x, s, y):
    ''' Функция expression(c) принимает 
        арифметическое выражение в качестве 
        аргумента и выводит результат этого выражения 
    '''
    if s in ('+', '-', '*', '/', '**' , '%'):
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
        return ("Неверный знак операции")


x = int(input("x = "))
s = input("Операция (+,-,*,/,**,%): ")
y = int(input("y = "))

print(expression(x, s, y))
