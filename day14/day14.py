def apply_mask(mask, value):

    binary_string = str(bin(int(value)))[2:]
    binary_string = '0'*(36-len(binary_string)) + binary_string
    binary_string=list(binary_string)

    for ch in range(36):
        if not mask[ch] == "X":
            binary_string[ch] = mask[ch]

    binary_string = "".join(binary_string)
    return int(binary_string,2)

mask = 'X'*36
mem = {}

with open('input.txt') as f:
    program = [d.split(" = ") for d in f.read().split('\n')]

for line in program:
    if line[0] == "mask":
        mask = line[1]
    else:
        loc = line[0].split('[')[1][:-1]
        value = apply_mask(mask, line[1])
        mem[loc]=value

print(sum([k for _,k in mem.items()]))


