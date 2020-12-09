with open('input.txt') as f:
    seq = [int(d) for d in f.read().split('\n')]

print(seq)

preamble=25
len_seq = len(seq)

def check_number(i, seq):
    num = seq[i]
    for j in range(preamble):
        chk = seq[i-j-1]
        if num-chk in (seq[i-preamble:i-1]) and not num-chk == chk:
            print("{} = {} + {}".format(num, chk, num-chk))
            return True
    return False


for i in range(preamble,len_seq):
    if not check_number(i, seq):
        print("First number to fail test is: {}".format(seq[i]))
        break

