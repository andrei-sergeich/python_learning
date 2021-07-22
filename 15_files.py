# Задание 1

print("Задание 1")

f = open('task_file copy.txt')

def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter+=1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails


lst = []
for line in f:
    lst.append(line.split(", "))


ls_named = []
id = 1
while id < len(lst):
    # if (len(ls[j][1]) > 0 and len(ls[j][2]) > 0 and len(ls[j][4]) > 0 and 
    # len(ls[j][3]) == 7 and ls[j][3].isdigit()):
    if (lst[id][1] != lst[id][2] != lst[id][4] and len(lst[id][3]) == 7 and 
            lst[id][3].isdigit() and lst[id][1].istitle() and lst[id][2].istitle()):
        ls_named.append(lst[id][1:3])
    id += 1


emails_lst = email_gen(ls_named)


i1 = 1
i2 = 0
while i2 < len(emails_lst):
    if lst[i1][2][0:5] == emails_lst[i2][0:5]:
        lst[i1].insert(0, emails_lst[i2])
        lst[i1].pop(1)
        i1 += 1
        i2 += 1
    else:
        lst[i1].insert(0, '')
        lst[i1].pop(1)
        i1 += 1

f.close()


f = open('task_file copy.txt', 'w')
for i in range(len(lst)):
    f.write(", ".join(lst[i]))

f.close()