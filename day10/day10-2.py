from math import comb
from itertools import groupby

with open('input.txt') as f:
    jolts = [int(d) for d in f.read().split('\n')]

outlet = 0
device = max(jolts)+3
jolts.extend([outlet, device])

jolts.sort()
diff = [jolts[i+1]-jolts[i] for i in range(len(jolts)-1)]

counts = [(i, len(list(g))) for i, g in groupby(diff)]

combos = 1
for c in counts:
    if c[0] == 1:
        tt = comb(c[1],2)+1
        combos *= tt

print(combos)

