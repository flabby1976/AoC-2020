password_list=[]
with open('input.txt', 'r') as fd:
    for line in fd:
        password_list.append(line.strip('\n'))

valid_num = 0
for pwd_test in password_list:
    # print(pwd_test)
    d = pwd_test.split(": ")
    rule = d[0]
    pwd = d[1]
    
    # print(rule)
    # print(pwd)

    d = rule.split(" ")
    nums = d[0]
    ch = d[1]

    # print(nums)
    # print(ch)

    d = nums.split("-")
    pos1 = int(d[0])
    pos2 = int(d[1])

    # print(pos1)
    # print(pos2)

    try:
        if (pwd[pos1-1]==ch) != (pwd[pos2-1]==ch):
            valid_num = valid_num + 1
            print("Success: " +pwd_test)
            print("pos: "+ d[0] + " ch: " + pwd[pos1-1])
            print("pos: "+ d[1] + " ch: " + pwd[pos2-1])
    except IndexError:
        continue


print(valid_num)