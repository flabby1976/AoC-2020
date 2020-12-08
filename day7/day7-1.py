
def get_options(rules, looking_for):
    options = []
    for rule in rules:
        container = rule.split(' bags contain ')[0]
        containing = rule.split(' bags contain ')[1]
        if looking_for in containing:
            options.append(container)
    return options

with open('input.txt') as f:
    rules = f.read().split('\n')

to_check = ['shiny gold']
options=set()
checked=[]

while to_check:
    checked.append(to_check)
    looking_for = to_check.pop()
    # print('Looking for: {}'.format(looking_for))
    fil = get_options(rules, looking_for)
    # print('Found: {}'.format(fil))
    options.update(fil)
    for o in fil:
        if o not in checked:
            to_check.append(o)
    # print('Options: {}'.format(options))

print('\n{}'.format(options))
print('\n{}'.format(len(options)))
