neighbours = {'e':(2,0), 'se':(1,-1), 'sw':(-1, -1), 'w':(-2,0), 'nw':(-1,1), 'ne':(1,1)}

def tile_from_route(r):
    x=0
    y=0
    for s in r:
        dx, dy = neighbours[s]
        x += dx
        y += dy
    return (x,y)

def get_my_neighbours(t):
    x, y = t
    return set((x+dx, y+dy) for dx, dy in neighbours.values())


with open('input.txt') as f:
    routestrings = f.read().split('\n')
    black_tiles = set()
    for rs in routestrings:
        route = []
        n = 0
        while n < len(rs):
            if rs[n] in ['n', 's']:
                route.append(rs[n]+rs[n+1])
                n += 1
            else:
                route.append(rs[n])
            n += 1

        tile = tile_from_route(route)                
 
        if tile in black_tiles:
            black_tiles -= {tile}
        else:
            black_tiles |= {tile}

print(black_tiles)

for day in range(1,100+1):
    new_tiles = set()
    for tile in black_tiles:
        my_neighbours = get_my_neighbours(tile)
        black_neighbours = my_neighbours & black_tiles
        white_neighbours = my_neighbours - black_neighbours
        if len(black_neighbours) > 0 and len(black_neighbours) < 3:
            new_tiles |= {tile}
        for w in white_neighbours:
            wn = get_my_neighbours(w)
            bn = wn & black_tiles
            if len(bn) == 2:
                new_tiles |= {w}
    
    black_tiles = new_tiles
    print("Day {}: {}".format(day, len(black_tiles)))
