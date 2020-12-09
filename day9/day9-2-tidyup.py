with open('input.txt') as f:
    seq = [int(d) for d in f.read().split('\n')]

target_num = 29221323

len_seq = len(seq)

for i in range(len_seq):
    for j in range(i+2, len_seq):
        block = seq[i:j]
        summ = sum(block)
        if summ == target_num:
            print("Success!")
            print("Min: {} Max: {} Sum(Min, Max): {}".format(min(block), max(block), min(block)+max(block)))
            break
        elif summ > target_num:
            break







