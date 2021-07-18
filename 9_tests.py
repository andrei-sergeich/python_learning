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

dig_lst = [1, 5, 1, 5, 1]
more_lst = []
i = 1
while i < len(dig_lst):
    if dig_lst[i] > dig_lst[i - 1]:
        more_lst.append(dig_lst[i])
    i += 1
print(*more_lst, sep=", ")

print()
print("Задание 2. Вариант решения №2")

dig_lst = [1, 2, 3, 4, 5]
more_lst = []
for i in range(1, len(dig_lst)):
    if dig_lst[i] > dig_lst[i - 1]:
        more_lst.append(dig_lst[i])
    # i += 1
print(*more_lst, sep=", ")

print()
print("----------------------------")
print()

# Задание 3
# Задан список с числами. Напишите программу, которая меняет
# местами наибольший и наименьший элемент и выводит новый список.
print("Задание 3. Вариант решения №1")

dig_lst = [-5, 5, 10]
swap_lst = dig_lst.copy()
max_val = max(dig_lst)
min_val = min(dig_lst)
i = 0

while i < len(swap_lst):
    if swap_lst[i] == max_val:
        swap_lst[i] = min_val
    elif swap_lst[i] == min_val:
        swap_lst[i] = max_val
    i += 1

print(*swap_lst, sep=", ")

print()
print("Задание 3. Вариант решения №2")

dig_lst = [3, 4, 5, 2, 1]
swap_lst = dig_lst.copy()
index_of_min = 0
index_of_max = 0

for i in range(len(swap_lst)):
    if swap_lst[i] > swap_lst[index_of_max]:
        index_of_max = i
    if swap_lst[i] < swap_lst[index_of_min]:
        index_of_min = i

swap_lst[index_of_min], swap_lst[index_of_max] = swap_lst[index_of_max], swap_lst[index_of_min]
print(*swap_lst, sep=", ")

print()

print("Задание 3. Вариант решения №3")

dig_lst = [1, 2, 3, 4, 5, 6, 7]
swap_lst = dig_lst.copy()
max_val_index = swap_lst.index(max(dig_lst))
min_val_index = swap_lst.index(min(dig_lst))

swap_lst[min_val_index], swap_lst[max_val_index] = swap_lst[max_val_index], swap_lst[min_val_index]

print(*swap_lst, sep=", ")
