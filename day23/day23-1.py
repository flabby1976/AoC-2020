cup_labeling = '215694783'
current_cup = cup_labeling[0]
len_cups = len(cup_labeling)

cups_ints = [int(d) for d in cup_labeling]
cups_max = max(cups_ints)
cups_min = min(cups_ints)

cups = list(cup_labeling)
for i in range(100):
    print("\n-- move {} --".format(i+1))
    k = cups.index(current_cup)
    cupstring = ''.join(cups[:k])+'('+cups[k]+')'+''.join(cups[(k+1):])
    print("cups: {}". format(cupstring))
    k1 = (k+1) % len_cups
    k2 = (k+2) % len_cups
    k3 = (k+3) % len_cups
    c1 = cups[k1]
    c2 = cups[k2]
    c3 = cups[k3]
    print("pick up: {}, {}, {}".format(c1, c2, c3))
    dest = int(current_cup) - 1
    if dest < cups_min:
        dest = cups_max
    while str(dest) in [c1, c2, c3]:
        dest -= 1
        if dest < cups_min:
            dest = cups_max
    print("destination: {}".format(dest))
    cups.remove(c1)
    cups.remove(c2)
    cups.remove(c3)
    k = cups.index(str(dest))
    cups = cups[:k+1]+[c1, c2, c3]+cups[k+1:]
    k = cups.index(current_cup)
    current_cup = cups[(k+1)%len_cups]

k = cups_ints.index(current_cup)
cupstring = ''.join([str(d) for d in cups_ints[:k]])+'('+str(cups_ints[k])+')'+''.join([str(d) for d in cups_ints[(k+1):]])
print("\n -- final --")
print("cups: {}". format(cupstring))

ans=''
k = cups.index('1')
for i in range(len_cups-1):
    ans += cups[(k+1+i)%len_cups]

print(ans)







