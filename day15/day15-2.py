import time
start_time = time.time()

start_list = [11,18,0,20,1,7,16]
end_num = 30000000

#use a dict to store the last positions of the numbers
num_list = {}

# store the start list first
s = len(start_list)
for i in range(s-1):
    num_list[start_list[i]] = i+1

last_number = start_list[-1]
for i in range(s+1, end_num+1):

    if last_number not in num_list:
        next_number = 0
    else:
        next_number = (i - 1) - num_list[last_number]
 
    num_list[last_number] = i-1
 
    last_number = next_number

print("The {}th number spoken is {}".format(end_num, last_number))
print("--- {} seconds ---".format(time.time() - start_time))