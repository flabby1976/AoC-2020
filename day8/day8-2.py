with open('input.txt') as f:
    myprogram = f.read().split('\n')

# print(program)

def parse_line(instruction):
    operator = instruction[0:3]
        # print(operator)
    argument = instruction[4:]
        # print(argument)
    return (operator, argument)
     

def test_program(program):
    acc = 0
    pc = 0
    ran = []

    while pc < len(program):
        operator, argument = parse_line(program[pc])
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
            return None

    return acc

for line in range(len(myprogram)):
    operator, argument = parse_line(myprogram[line])
    if operator == "nop":
        myprogram[line] = "jmp " + argument
    elif operator == "jmp":
        myprogram[line] = "nop " + argument
    else:
        continue
    print("checking line {}".format(line))
    acc = test_program(myprogram)
    if acc:
        print("SUCCESS!")
        print(acc)
        break
    if operator == "jmp":
        myprogram[line] = "jmp " + argument
    elif operator == "nop":
        myprogram[line] = "nop " + argument

