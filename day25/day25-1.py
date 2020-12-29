with open('input.txt') as f:
    public_keys = [int(k) for k in f.read().split('\n')]

print(public_keys)

def transform(subject_number, value):
    value *= subject_number
    return value % 20201227

def find_loop_size(key):
    value = 1
    n = 0
    while True:
        value = transform(7, value)
        n = n+1
        if value == key:
            return n

loopsize = find_loop_size(public_keys[0])
print("loopsize for key {} is: {}".format(public_keys[0], loopsize))

val = 1
for l in range(loopsize):
    val = transform(public_keys[1], val)

print(val)

loopsize = find_loop_size(public_keys[1])
print("loopsize for key {} is: {}".format(public_keys[1], loopsize))

val = 1
for l in range(loopsize):
    val = transform(public_keys[0], val)

print(val)

