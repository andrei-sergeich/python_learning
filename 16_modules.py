# Задание 1
# В заданиях к разделу "Строки" одна из задач состояла в написании 
# программы, # проверяющей надежность пароля. В данном упражнении 
# вам необходимо написать функцию, которая будет генерировать тот 
# самый надежный пароль случайным образом. Модуль random как раз 
# поможет вам в этом. 
# Давайте вспомним когда пароль считается надежным:
# 1) Пароль содержит не менее 12 символов
# 2) Пароль содержит хотя бы одну заглавную букву
# 3) Пароль содержит хотя бы одну строчную букву
# 4) Пароль содержит хотя бы одну цифру
# 5) Пароль содержит хотя бы один спецсимвол

print("Задание 1")

import random

dig_sym = "1234567890"
sp_sym = "!@#$%^&*()-+"
lo_lett_sym = "abcdefghijklmnopqrstuvwxyz"
up_lett_sym = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

passw_len = int(input("Введите дилну генерируемого пароля: "))

def pass_generator(lst):
    id = 0
    while id < passw_len - 6:
        lst.append(random.choice(lo_lett_sym))
        id += 1
    lst.append(random.choice(dig_sym))
    lst.append(random.choice(dig_sym))
    lst.append(random.choice(up_lett_sym))
    lst.append(random.choice(up_lett_sym))
    lst.append(random.choice(sp_sym))
    lst.append(random.choice(sp_sym))
    random.shuffle(lst)
    return lst

lst = []
s = "".join(pass_generator(lst))
print(s)
