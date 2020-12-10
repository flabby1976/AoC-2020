with open('input.txt') as f:
    seq = [int(d) for d in f.read().split('\n')]

target_num = 29221323

len_seq = len(seq)

j = 0
for i in range(len_seq):
    while j < len_seq:
        block = seq[i:j]
        summ = sum(block)
        if summ == target_num:
            print("Success!")
            print(i,j, summ)
            print(block])
            mini = min(block)
            maxi = max(block)
            print("Min: {} Max: {} Sum(Min, Max): {}".format(mini, maxi, mini+maxi))
            break
        elif summ > target_num:
            break
        j += 1








