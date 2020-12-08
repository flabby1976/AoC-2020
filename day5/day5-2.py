def decode_card(code):
    
    row = 0
    k = 64
    for ch in code[:7]:
        if ch == 'B':
            row = row + k
        k = int(k / 2)
    
    col = 0
    k = 4
    for ch in code[-3:]:
        if ch == 'R':
            col = col + k
        k = int(k / 2)

    return (row,col)

seatid_list = []
with open('input.txt', 'r') as fd:
    for line in fd:
        card = line.strip()
        (row, col) = decode_card(card)
        seat_id = row * 8 + col
        seatid_list.append(seat_id)

for my_row in range(128):
    for my_col in range(8):
        my_seatid = my_row * 8 + my_col
        if my_seatid not in seatid_list and my_seatid - 1 in seatid_list and my_seatid + 1 in seatid_list:
            print (my_seatid)

