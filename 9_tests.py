# Задание 1
# Задан список с числами. Напишите программу, которая выводит 
# все элементы списка с четными индексами в виде нового списка.
print("Задание 1. Вариант решения №1")

# s = input("Введите числа через пробел ")
# s_lst = s.split(" ")
# dig_lst = [int(d) for d in s_lst]
# even_lst = []
# for i in dig_lst:
#     if dig_lst.index(i) % 2 == 0:
#         even_lst.append(i)
# print(*even_lst, sep=", ")

print()
print("Задание 1. Вариант решения №2")
dig_lst = [90, 45, 3, 43]
even_lst = []
for i in dig_lst:
    if dig_lst.index(i) % 2 == 0:
        even_lst.append(i)
print(*even_lst, sep=", ")

print()
print("----------------------------")
print()

# Задание 2
# Задан список с числами. Напишите программу, которая выводит 
# все элементы списка, которые больше предыдущего, в виде отдельного списка.
print("Задание 2. Вариант решения №1")

dig_lst = [90, 45, 3, 43]
more_lst = []
i = 1
while i < len(dig_lst):
# for i in dig_lst:
    if dig_lst[i] > dig_lst[i - 1]:
        more_lst.append(i)
    i += 1
print(*more_lst, sep=", ")

print()
print("----------------------------")
print()