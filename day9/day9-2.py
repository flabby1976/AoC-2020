with open('input.txt') as f:
    seq = [int(d) for d in f.read().split('\n')]

target_num = 29221323

len_seq = len(seq)

for i in range(len_seq):
    summ = 0
    j = 0
    while i+j < len_seq:
        j += 1
        summ = sum(seq[i:i+j])
        if summ == target_num:
            print("Success!")
            print(i,j, summ)
            print(seq[i:i+j])
            mini = min(seq[i:i+j])
            maxi = max(seq[i:i+j])
            print("Min: {} Max: {} Sum(Min, Max): {}".format(mini, maxi, mini+maxi))
            break
        elif summ > target_num:
            break







