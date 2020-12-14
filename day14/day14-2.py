import copy

def set_location(a,loc, val):

    if "X" not in loc:
        loc_dec = int("".join(loc),2)
        mem[loc_dec]=val
    else:
        try_loc = copy.copy(loc)
        # go the first "X" in the location and run again with 0 and then 1
        ch = try_loc.index("X")
        try_loc[ch] = "0"
        set_location(a, try_loc, value)
        try_loc[ch] = "1"
        set_location(a, try_loc, value)

mask = ['0']*36

mem = {}

with open('input.txt') as f:
    program = [d.split(" = ") for d in f.read().split('\n')]

for line in program:
    if line[0] == "mask":
        mask = list(line[1])
    else:
        location = line[0].split('[')[1][:-1]
        value = int(line[1])

        binary_string = str(bin(int(location)))[2:]
        binary_string = '0'*(36-len(binary_string)) + binary_string

        location=list(binary_string)

        for ch in range(36):
            if  mask[ch] == "1":
                location[ch] = "1"
            elif mask[ch] == "X":
                location[ch] = "X"

        set_location("", location, value)

print(sum([k for _,k in mem.items()]))


