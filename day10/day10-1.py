from collections import Counter

with open('test2.txt') as f:
    jolts = [int(d) for d in f.read().split('\n')]

outlet = 0
device = max(jolts)+3
jolts.extend([outlet, device])

print(device)

jolts.sort()
diff = [jolts[i+1]-jolts[i] for i in range(len(jolts)-1)]

counts = Counter(diff)

print(counts)
print(counts[1]*counts[3])
