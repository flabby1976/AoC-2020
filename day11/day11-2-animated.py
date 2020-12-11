import numpy as np 
import matplotlib.pyplot as plt 

def disp_seats():
    for r in seats:
        print(r)
    print("\n")

def get_seat(r,c):
    if r < 0 or c < 0:
        return ""
    try:
        s = seats[r][c]
    except IndexError:
        s = ""
    return s

def adjacent_seats_occupied(row, col):
    t = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    adj=0
    for r in t:
        s = 0
        still_looking = True
        while still_looking:
            s += 1
            test = get_seat(row+s*r[0],col+s*r[1])
            if test == "#":
                adj += 1
                still_looking = False
            elif test == "" or test == "L":
                still_looking = False

    return adj

def make_it_np(seats):
    out = []
    for row in seats:
        n = []
        for seat in row:
            if seat == "L":
                n.append(.5)
            elif seat == "#":
                n.append(1)
            else:
                n.append(0)
        out.append(n)
    
    return np.array(out)

with open('input.txt') as f:
    seats = [[k for k in d] for d in f.read().split('\n')]

seat_rows = len(seats)
seats_per_row = len(seats[0])

figure = plt.figure() 
axes = figure.add_subplot(111) 

# convert seats to a np_array
random_array = make_it_np(seats)

# using the matshow() function  
caxes = axes.imshow(random_array, vmin=0, vmax=1) 
# figure.colorbar(caxes) 

plt.axis('off')

plt.ion()
plt.show()

stable = False
while not stable:
    new_seats = []
    for seat_row in range(seat_rows):
        new_seats.append([" "]*seats_per_row)
        for seat in range(seats_per_row):
            adj = adjacent_seats_occupied(seat_row,seat)

            if seats[seat_row][seat] == "L" and adj == 0:
                    new_seats[seat_row][seat] = "#"

            elif seats[seat_row][seat] == "#" and adj > 4:
                    new_seats[seat_row][seat] = "L"

            else:
                new_seats[seat_row][seat] = seats[seat_row][seat]

    
    random_array = make_it_np(new_seats)
    caxes.set_data( random_array )

    plt.pause(.1)

    if not new_seats == seats:
        seats = new_seats
    else:
        stable = True

c=0
for r in seats:
    c += r.count("#")
print(c)

input("Press Enter to continue ...")

            


