import time
start_time = time.time()

start_list = [11,18,0,20,1,7,16]
end_num = 30000000

# Use a dict to store the last positions of the numbers.
# Store the start list first
s = len(start_list)
num_list = {start_list[i] : i+1 for i in range(s-1)}

number = start_list[-1]
for i in range(s, end_num):

    if number not in num_list:
        next_number = 0
    else:
        next_number = i - num_list[number]
 
    num_list[number] = i
    number = next_number

print("The {}th number spoken is {}".format(end_num, number))
print("--- {} seconds ---".format(time.time() - start_time))