with open('input.txt') as f:
    program = f.read().split('\n')

# print(program)

acc = 0
pc = 0
ran = []

while pc < len(program):
    instrauction = program[pc]
    operator = instrauction[0:3]
    # print(operator)
    argument = instrauction[4:]
    # print(argument)
    print("pc: {} op: {} arg: {} acc: {}".format(pc, operator, argument, acc))
    if operator == "acc":
        acc += int(argument)
        pc += 1
    elif operator == "jmp":
        pc += int(argument)
    else:
        pc += 1
    
    if pc not in ran:
        ran.append(pc)
    else:
        print("INFINITE LOOP!!")
        print("acc = {}".format(acc))
        break

