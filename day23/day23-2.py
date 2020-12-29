import time
start_time = time.time()

cups_max = 1000000
cups_min = 1
next_cup = {k: k + 1 for k in range(cups_min, cups_max+1)}

# 215694783
starting_cups = {
    2: 1,
    1: 5,
    5: 6,
    6: 9,
    9: 4,
    4: 7,
    7: 8,
    8: 3,
    3: 10,
    1000000: 2,
}
current_cup = 2

# Example input
# starting_cups = {
#     3: 8,
#     8: 9,
#     9: 1,
#     1: 2,
#     2: 5,
#     5: 4,
#     4: 6,
#     6: 7,
#     7: 10,
#     1000000: 3,
# }
# current_cup = 3

next_cup.update(starting_cups)

for i in range(10000000):
    c1 = next_cup[current_cup]
    c2 = next_cup[c1]
    c3 = next_cup[c2]

    dest = current_cup - 1
    if dest < cups_min:
        dest = cups_max
    while dest in [c1, c2, c3]:
        dest -= 1
        if dest < cups_min:
            dest = cups_max

    next_cup[current_cup] = next_cup[c3]
    next_cup[c3] = next_cup[dest]
    next_cup[dest] = c1

    current_cup = next_cup[current_cup]

c = next_cup[1]
d = next_cup[c]
print("{} x {} = {}".format(c,d,c*d))

print("--- %s seconds ---" % (time.time() - start_time))
