def decode_card(code):
    
    row = 0
    k = 64
    for ch in code[:7]:
        print(ch)
        if ch == 'B':
            row = row + k
        k = int(k / 2)
    
    col = 0
    k = 4
    for ch in code[-3:]:
        print(ch)
        if ch == 'R':
            col = col + k
        k = int(k / 2)

    return (row,col)


(row,col) = decode_card("BFFFBBFRRR")
print((row,col), row*8+col)