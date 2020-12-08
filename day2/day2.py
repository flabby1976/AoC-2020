password_list=[]
with open('input.txt', 'r') as fd:
    for line in fd:
        password_list.append(line.strip('\n'))

valid_num = 0
for pwd_test in password_list:
    print(pwd_test)
    d = pwd_test.split(": ")
    rule = d[0]
    pwd = d[1]
    
    print(rule)
    print(pwd)

    d = rule.split(" ")
    nums = d[0]
    ch = d[1]

    print(nums)
    print(ch)

    d = nums.split("-")
    mini = int(d[0])
    maxi = int(d[1])

    print(mini)
    print(maxi)
    
    count=0
    for i in pwd:
        if i == ch:
            count=count+1
    
    if not count < mini:
        if not count > maxi:
            valid_num = valid_num + 1

print(valid_num)