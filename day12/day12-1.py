def rotate(current, degrees):
    directions = ["N", "E", "S", "W"]
    c = (directions.index(current) + int(degrees / 90)) % 4
    new_direction = directions[c]
   
    return new_direction

moves = {
            "N": (0,1),
            "S": (0,-1),
            "E": (1,0),
            "W": (-1,0)
        }

direction = 'E'
x=0
y=0

with open('input.txt') as f:
    route = [(d[0], int(d[1:])) for d in f.read().split('\n')]

for action, value in route:

    if action == "R":
        direction = rotate(direction, value)
        continue

    if action == "L":
        direction = rotate(direction, -1*value)
        continue

    if action == "F":
        action = direction

    dx, dy = moves[action]
    x += dx * value
    y += dy * value

print ("End position is x={} y={}".format(x,y))
print ("Manhatten distance = {}".format(abs(x)+abs(y)))
