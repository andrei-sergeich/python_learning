# Задание 1

print("Задание 1")

import re

def gen(passw_len):
    import random

    lst = []
    dig_sym = "1234567890"
    sp_sym = "!@#$%^&*()-+"
    lo_lett_sym = "abcdefghijklmnopqrstuvwxyz"
    up_lett_sym = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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

    passw = "".join(pass_generator(lst))
    return (passw)

def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter+=1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails


lst = []
ls_named = []
ls_non_val = []

f = open('./final_project/data_file.txt')
for line in f:
    lst.append(line.split(", "))
f.close()

for i in range(len(lst)):
    for j in range(len(lst[i])):
        lst[i][j]=lst[i][j].replace(' ','')

id = 1
ls_non_val.append(lst[0]) # Добавляем заголовок "EMAIL, NAME, LAST_NAME, TEL, CITY\n"
while id < len(lst):
    if (re.findall(r'^$|\W|\d|NAME', lst[id][1]) or 
            re.findall(r'[wrtplkhgfdszxcvbnm][wrtplkhgfdszxcvbnm][wrtplkhgfdszxcvbnm][wrtplkhgfdszxcvbnm]', lst[id][1]) or 
            re.findall(r'^$|\W|\d|NAME', lst[id][2]) or 
            re.findall(r'0......|\D|^$', lst[id][3]) or 
            len(lst[id][3]) != 7 or 
            re.findall(r'\W+\n$|\d|^$', lst[id][4])
        ):
            ls_non_val.append(lst[id])
    else:
        ls_named.append([lst[id][1], lst[id][2]])
    id += 1

emails_lst = email_gen(ls_named)

i1 = 1
i2 = 0
while i2 < len(emails_lst): # Записываем в оригинальный список адреса электронной почты
    if lst[i1][2][0:5] == emails_lst[i2][0:5]: # Если первые 4 символа фамилии и адреса эл.почты равны,
        lst[i1][0] = emails_lst[i2] #то записываем в 0 индекс адрес эл.почты
        i1 += 1
        i2 += 1
    else:
        lst.pop(i1) # полностью удаляем подсписок из оригинального списка


f_1 = open('./final_project/new_file.txt', 'w')
f_2 = open('./final_project/non_val_file.txt', 'w')

f_1.write('EMAIL, PASSWORD, NAME, LAST_NAME, TEL, CITY\n')
for row in range(1, len(lst)):
    f_1.write(lst[row][0]+', '+gen(15)+', '+lst[row][1]+', '+lst[row][2]+', '+lst[row][3]+', '+lst[row][4])

for row in range(len(ls_non_val)):
    f_2.write(", ".join(ls_non_val[row]))

f_1.close()
f_2.close()
