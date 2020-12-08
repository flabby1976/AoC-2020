expense_list=[]
with open('input.txt', 'r') as fd:
    for line in fd:
        expense_list.append(int(line.strip('\n')))

for i in expense_list:
    expense_list.remove(i)
    if 2020-i in expense_list:
        print(i, 2020-i, i*(2020-i))
        break

expense_list=[]
with open('input.txt', 'r') as fd:
    for line in fd:
        expense_list.append(int(line.strip('\n')))
        
for i in expense_list:
    expense_list.remove(i)
    for j in expense_list:
        if 2020-i-j in expense_list:
            print(i, j, 2020-i-j, i*j*(2020-i-j))
            break
