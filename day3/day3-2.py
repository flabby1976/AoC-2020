my_map=[]
with open('input.txt', 'r') as fd:
    for line in fd:
        my_map.append(line.strip('\n'))

map_width = len(my_map[0])
map_height = len(my_map)

prod = 1
ans = ""

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

for slope in slopes: 

    print("Slope: {}".format(slope))

    num_trees = 0

    row = 0
    col = 0

    while True:
        row = row + slope[1]
        col = (col + slope[0]) % map_width
        # print(row)
        # print(col)
        try:
            # print(my_map[row][col])
            if my_map[row][col] == "#":
                num_trees = num_trees + 1
        except IndexError:
            break


    print("Number of trees: {}".format(num_trees))
    print("=================")

    prod = prod * num_trees

    ans = ans + str(num_trees) + " * " 

print("\n{} = {}".format(ans[0:-3], prod))

