#!/usr/bin/python

import modules

passw = modules.gen(20)

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

if forb_sym is False:
    if dig_sym_fl == sp_sym_fl == up_lett_fl == lo_lett_fl == True and \
            len(passw) >= 12:
        print("Сильный пароль.")
    else:
        mes_lst = []
        print("Слабый пароль. Рекомендации:", end='')
        if len(passw) < 12:
            passw_len = " увеличить число символов - " + str(12 - len(passw))
            mes_lst.append(passw_len)
        if dig_sym_fl is False:
            mes_lst.append("добавить 1 цифру")
        if sp_sym_fl is False:
            mes_lst.append("добавить 1 спецсимвол")
        if lo_lett_fl is False:
            mes_lst.append("добавить 1 строчную букву")
        if up_lett_fl is False:
            mes_lst.append("добавить 1 заглавную букву")
        mes = ", ".join(mes_lst)
        print(mes)
