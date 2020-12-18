def get_next_block(s):
    start = s.find('(')
    if start == -1:
        return []
    
    depth = 1
    for stop, ch in enumerate(s[(start+1):]):
        if ch == ')':
            depth -= 1
        elif ch == '(':
            depth += 1
        if depth == 0:
            break

    block = s[(start+1):(stop+start+1)]

    return block

def eval_exp(s):

    while '(' in s:
        block = get_next_block(s)
        a = eval_exp(block)
        s = s.replace('('+block+')',str(a))

    exp = s.split(' ')

    # Deal with the addition first!
    while "+" in exp:
        i = exp.index("+")
        a = int(exp[i-1])+int(exp[i+1])
        exp[i-1] = str(a)
        exp = exp[:i] + exp[i+2:]

    # Only multiplication left!
    a = int(exp[0])
    for i in range(1,len(exp),2):
        a *= int(exp[i+1])

    return a

with open('input.txt') as f:
    ans = [eval_exp(d) for d in f.read().split('\n')]

print(sum(ans))
