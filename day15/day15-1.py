import time
start_time = time.time()

def next_number(num_list):
    last_number = num_list[-1]
    if last_number not in num_list[:-1]:
        return 0
    else:
        # Surely we dont't really need to do this search every time!
        find = [index for index, value in enumerate(num_list) if value == last_number]
        age = find[-1]-find[-2]
        return age

number_list = [11,18,0,20,1,7,16]

s = len(number_list)
end_num = 2020

for i in range(s+1, end_num+1):
    num = next_number(number_list)
    number_list.append(num)

print("The {}th number spoken is {}".format(end_num, number_list[-1]))
print("--- {} seconds ---".format(time.time() - start_time))