# Задание 1
# Дана строка: Abraсadabra
# Требуется:

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

# Задание 2
# Напишите код, который обрабатывает строковые данные 
# и возвращает их с первыми заглавными буквами в каждом слове.
# Слова в строке отделены пробелами. 
# Каждое слово после обработки должно быть с заглавной буквы, 
# только, если первый символ слова - буква, 
# в случае типа '3amg' код не должен менять буквы.
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

passw = 'qwEe*rtyдьЬ'
num_sym = '1234567890'
sp_sym = '!@#$%^&*()-+'
lo_lett_sym = 'abcdefghijklmnopqrstuvwxyz'
up_lett_sym = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num_sym_fl = False
sp_sym_fl = False
up_lett_fl = False
lo_lett_fl = False
for i in passw:
    # print(sp_sym.find(i))
    if sp_sym.find(i) is not -1:
        print(sp_sym.find(i))
        sp_sym_fl = True
    if num_sym.find(i) is not -1:
        print(num_sym.find(i))
        num_sym_fl = True
    # print(passw.islower())
    if lo_lett_sym.find(i) is not -1:
        print(lo_lett_sym.find(i))
        lo_lett_fl = True
    if up_lett_sym.find(i) is not -1:
        print(up_lett_sym.find(i))
        up_lett_fl = True
print(sp_sym_fl)
print(num_sym_fl)
print(lo_lett_fl)
print(up_lett_fl)