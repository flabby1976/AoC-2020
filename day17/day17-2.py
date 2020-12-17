deltas = [-1,0,1]
neighbours = [(x, y, z, w) for x in deltas for y in deltas for z in deltas for w in deltas]
neighbours.remove((0,0,0,0))

def get_neighbours(cube):
    (x, y, z, w) = cube
    return set((x+dx, y+dy, z+dz, w+dw) for (dx, dy, dz, dw) in neighbours)

def next_active(current_active):
    next = set()
    for active_cube in current_active:
        nearest = get_neighbours(active_cube)
        if len(nearest.intersection(current_active)) in [2,3]:
            next.add(active_cube)
        for n in nearest:
            if n not in current_active:
                nn = get_neighbours(n)
                if len(nn.intersection(current_active)) == 3:
                    next.add(n)
    return next

current_active = set()
with open('input.txt') as f:
    inp = [d for d in f.read().split('\n')]
for y, line in enumerate(inp):
    for x, ch in enumerate(line):
        if ch == "#":
            current_active.add((x,y,0,0))

for cycle in range(6):
    current_active = next_active(current_active)

    
print(len(current_active))
