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

boarding_passes=[]
with open('input.txt', 'r') as fd:
    for line in fd:
        boarding_passes.append(line.strip('\n'))

max_code = 0
for card in boarding_passes:
    (row, col) = decode_card(card)
    seat_id = row * 8 + col
    max_code = max(max_code, seat_id)

print(max_code)