def tile_from_route(r):
    x=0
    y=0
    for s in r:
        if s == 'e':
            x += 2
        if s == 'w':
            x -= 2
        if s == 'ne':
            x += 1
            y += 1
        if s == 'nw':
            x -= 1
            y += 1
        if s == 'se':
            x += 1
            y -= 1
        if s == 'sw':
            x -= 1
            y -= 1

    return (x,y)       

with open('test.txt') as f:
    routestrings = f.read().split('\n')
    black_tiles = []
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
            black_tiles.remove(tile)
        else:
            black_tiles.append(tile)

print(black_tiles)
print(len(black_tiles))