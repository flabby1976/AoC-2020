my_map=[]
with open('input.txt', 'r') as fd:
    for line in fd:
        my_map.append(line.strip('\n'))

map_width = len(my_map[0])
map_height = len(my_map)
num_trees = 0

row = 0
col = 0

while row < map_height - 1:
    row = row + 1
    col = (col + 3) % map_width
    # print(row)
    # print(col)
    print(my_map[row][col])
    if my_map[row][col] == "#":
        num_trees = num_trees + 1


print(num_trees)

