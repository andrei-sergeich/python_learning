# Задание 1
# Дана строка: Abraсadabra
# Требуется:
print("Задание 1.")

# 1. Вывести третий символ этой строки.
s = "Abraсadabra"
print(s[2])

# 2. Вывести предпоследний символ этой строки.
print(s[-2])

# 3. Вывести первые пять символов этой строки.
print(s[:5])

# 4. Вывести строку, кроме последних двух символов.
print(s[:len(s) - 2])

# 5. Вывести все символы с четными индексами (считайте, что 0 - четный индекс).
print(s[::2])

# 6. Вывести все символы с нечетными индексами.
print(s[1::2])

# 7. Вывести все символы в обратном порядке.
print(s[::-1])

# 8. Вывести все символы строки через один в обратном порядке, начиная с последнего.
print(s[-1::-2])

# 9. Вывести длину данной строки.
print(len(s))

print()
print("----------------------------")
print()

# Задание 2
# Напишите код, который обрабатывает строковые данные 
# и возвращает их с первыми заглавными буквами в каждом слове.
# Слова в строке отделены пробелами. 
# Каждое слово после обработки должно быть с заглавной буквы, 
# только, если первый символ слова - буква, 
# в случае типа '3amg' код не должен менять буквы.
print("Задание 2. Вариант решения №1")

s = 'a1 2b  3   abc d3e r2D2'
naims = s.split(' ')
i = 0
while i < len(naims):
    if naims[i]:
        if naims[i][0].isalpha():
            naims[i] = naims[i][0].upper() + naims[i][1:]
    i += 1
s_with_upper = ' '.join(naims)
print(s_with_upper)
print()

# Можно решить другим способом)))
print("Задание 2. Вариант решения №2")
s = 'a1 2b  3   abc d3e r2D2'
s_up = s.title()
print(s_up)

print()
print("----------------------------")
print()

# Задание 3
# Пароль считается надежным, если его длина составляет не менее 12 символов, 
# при этом он должен содержать хотя бы одну заглавную букву, 
# хотя бы одну строчную букву, хотя бы одну цифру и хотя бы один спецсимвол. 
# Напишите код, который обрабатывает строковые данные и выводит сообщение о том, 
# надежен ли пароль или нет. В случае, если пароль не надежен, 
# код должен выдавать рекомендации для усиления надежности пароля.
# Цифры, которые можно использовать для пароля: '1234567890'
# Строчные буквы, которые можно использовать для пароля: 'abcdefghijklmnopqrstuvwxyz'
# Заглавные буквы, которые можно использовать для пароля: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Спецсимволы, которые можно использовать для пароля: '!@#$%^&*()-+'
print("Задание 3. Вариант решения №1")

passw = "Q123wer123tY"

dig_sym = "1234567890"
sp_sym = "!@#$%^&*()-+"
lo_lett_sym = "abcdefghijklmnopqrstuvwxyz"
up_lett_sym = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
all = dig_sym + sp_sym + lo_lett_sym + up_lett_sym

dig_sym_fl = sp_sym_fl = lo_lett_fl = up_lett_fl = forb_sym = False

for i in passw:
    if i not in all:
        print("Ошибка. Запрещенный спецсимвол")
        forb_sym = True
        break
    if i in dig_sym:
        dig_sym_fl = True
    if i in sp_sym:
        sp_sym_fl = True
    if i in lo_lett_sym:
        lo_lett_fl = True
    if i in up_lett_sym:
        up_lett_fl = True

if forb_sym == False:
    if dig_sym_fl == sp_sym_fl == up_lett_fl == lo_lett_fl == True and len(passw) >= 12:
        print("Сильный пароль.")
    else:
        print("Слабый пароль. Рекомендации:", end='')
        if len(passw) < 12:
            print(" увеличить число символов - " + str(12 - len(passw)), end='')
        if dig_sym_fl == False:
            print(", добавить 1 цифру", end='')
        if sp_sym_fl == False:
            print(", добавить 1 спецсимвол", end='')
        if lo_lett_fl == False:
            print(", добавить 1 строчную букву", end='')
        if up_lett_fl == False:
            print(", добавить 1 заглавную букву", end='')


print()
print("Задание 3. Вариант решения №2")
passw = "qwerty"

dig_sym = "1234567890"
sp_sym = "!@#$%^&*()-+"
lo_lett_sym = "abcdefghijklmnopqrstuvwxyz"
up_lett_sym = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
all = dig_sym + sp_sym + lo_lett_sym + up_lett_sym

dig_sym_fl = sp_sym_fl = lo_lett_fl = up_lett_fl = forb_sym = False

for i in passw:
    if i not in all:
        print("Ошибка. Запрещенный спецсимвол")
        forb_sym = True
        break
    if i in dig_sym:
        dig_sym_fl = True
    if i in sp_sym:
        sp_sym_fl = True
    if i in lo_lett_sym:
        lo_lett_fl = True
    if i in up_lett_sym:
        up_lett_fl = True

if forb_sym == False:
    if dig_sym_fl == sp_sym_fl == up_lett_fl == lo_lett_fl == True and len(passw) >= 12:
        print("Сильный пароль.")
    else:
        mes_lst = []
        print("Слабый пароль. Рекомендации:", end='')
        if len(passw) < 12:
            passw_len = " увеличить число символов - " + str(12 - len(passw))
            mes_lst.append(passw_len)
        if dig_sym_fl == False:
            mes_lst.append("добавить 1 цифру")
        if sp_sym_fl == False:
            mes_lst.append("добавить 1 спецсимвол")
        if lo_lett_fl == False:
            mes_lst.append("добавить 1 строчную букву")
        if up_lett_fl == False:
            mes_lst.append("добавить 1 заглавную букву")
        mes = ", ".join(mes_lst)
        print(mes)
