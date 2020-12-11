
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

with open('input.txt') as f:
    seats = [[k for k in d] for d in f.read().split('\n')]

seat_rows = len(seats)
seats_per_row = len(seats[0])

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

    if not new_seats == seats:
        seats = new_seats
    else:
        stable = True

disp_seats()

c=0
for r in seats:
    c += r.count("#")
print(c)


            


