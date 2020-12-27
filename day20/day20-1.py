def get_border(tile_id, side):
    a = [
        tiles[tile_id][0],
        ''.join([t[-1] for t in tiles[tile_id]]),
        tiles[tile_id][-1],
        ''.join([t[0] for t in tiles[tile_id]])
    ]
    return a[side-1]

def border_match(a, side, b):
    test = get_border(a, side)
    for s in [1, 2, 3, 4]:
        test2 = get_border(b, s)
        if test == test2:
            # print("{} side {} matches {} side {}".format(a, side, c, s))
            # print(test, test2)
            return True
        if test == test2[::-1]:
            # print("{} side {} matches {} side {} reversed".format(a, side, c, s))
            return True
    return False

with open('test.txt') as f:
    tiles_string = f.read().split('\n\n')

tiles={}
for t in tiles_string:
    tile_id, tile_text = t.split(':\n')
    tiles[tile_id] = [row for row in tile_text.split('\n')]


matches={}

for tile_id in tiles:

    # print("Placing {}".format(tile_id))


    matches[tile_id] = 0

    for side in [1, 2, 3, 4]:

        for c in tiles:

            if c == tile_id:
                # don't check yourself
                continue

            if border_match(tile_id, side, c):
                matches[tile_id] += 1
                # break

ans=1
for m in matches:
    if matches[m] == 2:
        num = int(m.split(' ')[1])
        ans *= num
        print(m)

print(ans)