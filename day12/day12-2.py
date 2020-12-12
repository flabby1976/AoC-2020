def rotate(way_x, way_y, degrees):
    # rotation matrices for clockwise 0, 90, 180, 270 degrees
    deltas=[(1,0,0,1), (0,1,-1,0), (-1,0,0,-1), (0,-1,1,0)]
    c = int(degrees / 90) % 4
    da, db, dc, dd = deltas[c]
    x = way_x*da + way_y*db
    y = way_x*dc + way_y*dd 
    return x, y

# translation vectors for N, S, E W moves
moves = {
            "N": (0,1),
            "S": (0,-1),
            "E": (1,0),
            "W": (-1,0)
        }

# N is + on y-axis, E is + on the x-axis 
ship_x = 0
ship_y = 0
way_x = 10
way_y = 1

with open('input.txt') as f:
    route = [(d[0], int(d[1:])) for d in f.read().split('\n')]

for action, value in route:

    print ("ship position is x={} y={}".format(ship_x,ship_y))
    print ("way position is x={} y={}".format(way_x,way_y))

    print(action, value)

    if action == "R":
        way_x, way_y = rotate(way_x, way_y, value)
        continue

    if action == "L":
        way_x, way_y = rotate(way_x, way_y, -1*value)
        continue

    if action == "F":
        ship_x += way_x * value
        ship_y += way_y * value
        continue

    dx, dy = moves[action]
    way_x += dx * value
    way_y += dy * value

print ("End position is x={} y={}".format(ship_x,ship_y))
print ("Manhatten distance = {}".format(abs(ship_x)+abs(ship_y)))
