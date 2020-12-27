def get_border(a, side):
    # side = 1, 2, 3, 4 for N, E, S, W of the tile 
    return [
        a[0],
        ''.join([t[-1] for t in a]),
        a[-1],
        ''.join([t[0] for t in a])
    ][side-1]

def disp_tile(a):
    for j in range(len(a)):
        print(a[j])
    print('\n')

def rotate(a):
    return [''.join([t[i] for t in a]) for i in range(len(a)-1,-1,-1)]

def flip(a):
    return [t[::-1] for t in a]

def adj_coords(coords, side):
    offsets = [(0,1), (1,0), (0,-1), (-1,0)]
    dx, dy = offsets[side-1]
    x, y = coords
    x += dx
    y += dy
    return (x,y)

def border_match(f, m):
    for side in [1, 2, 3, 4]:
        test = get_border(tiles[f], side)
        for _ in [0, 1]: # flips
            for _ in [0, 1, 2, 3]: # rotates
                test2 = get_border(tiles[m], (side+2)%4)
                if test == test2:
                    return side
                tiles[m] = rotate(tiles[m])
            tiles[m] = flip(tiles[m])
    return 0

with open('input.txt') as f:
    tiles_string = f.read().split('\n\n')

tiles={}
for t in tiles_string:
    tile_id, tile_text = t.split(':\n')
    tiles[tile_id] = [row for row in tile_text.split('\n')]

placed={}
to_place = list(tiles)

tile_id = to_place.pop()
placed[(0,0)] = tile_id

n = 0
xmax = -100
ymax = -100
xmin = 100
ymin = 100

while to_place:
    tile_id = to_place[n % len(to_place)]
    for c in placed.values():
        m = border_match(c, tile_id)
        if not m == 0:
            x, y = adj_coords(list(placed.keys())[list(placed.values()).index(c)], m)
            if (x,y) not in placed:
                xmax=max(x, xmax)
                xmin=min(x, xmin)
                ymax=max(y, ymax)
                ymin=min(y, ymin)
                placed[(x, y)] = tile_id
                to_place.remove(tile_id)
                break
    n = n +1

print("x: {} to {}, y: {} to {}".format(xmin, xmax, ymin, ymax))
corners = [placed[(xmin, ymin)], placed[(xmin, ymax)], placed[(xmax, ymin)], placed[(xmax, ymax)]]
print("Corners: {}".format(corners))
ans=1
for c in corners:
    num = int(c.split(' ')[1])
    print(c)
    ans *= num

print("Part 1: {}".format(ans))

first_tile = list(tiles.values())[0]
tile_y = len(list(tiles.values())[0])
tile_x = len(list(tiles.values())[0][0])
# print(tile_x, tile_y)

ystep = tile_y - 2
image = ['']*ystep*(ymax-ymin+1)
n=0
for y in range(ymax, ymin-1, -1):
    for yt in range(ystep):
        for x in range(xmin, xmax+1):
            tile_id = placed[(x,y)]
            image[n] += (tiles[tile_id][yt+1])[1:-1]
        n=n+1

def check_seamonster(x,y):
    seamonster =[(18,0),(0,1),(5,1),(6,1),(11,1),(12,1),(17,1),(18,1),(19,1),(1,2),(4,2),(7,2),(10,2),(13,2),(16,2)]

    for dx,dy in seamonster:
        try:
            if not image[y+dy][x+dx] == "#":
                return False
        except IndexError:
            return False
    for dx,dy in seamonster:
        tmp = list(image[y+dy])
        tmp[x+dx] ="0"
        image[y+dy] = ''.join(tmp)

    return True

Found = False
for _ in [0, 1]: # flips
    for _ in [0, 1, 2, 3]: # rotates
        for y in range(len(image)):
            for x in range(len(image[0])):
                if check_seamonster(x,y):
                    Found = True
        if Found:
            break
        image = rotate(image)
    if Found:
        break
    image = flip(image)


disp_tile(image)

cnt=0
for r in image:
    cnt += r.count("#")

print(cnt)







