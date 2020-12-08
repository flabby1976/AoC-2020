def num_bags(a, rules, bag):

    num = 0
    sub_bags = rules[bag]
    if not sub_bags:
        print(a+'{} bag contains no sub bags'.format(bag))
        return num

    print(a+'{} bag contains: {}'.format(bag, sub_bags))
    for btype, bcount in sub_bags.items():       
        num = num + int(bcount)*(1 + num_bags(a+"    ", rules, btype))
        
    print(a+'One {} bag contains a total of {} other sub bags'.format(bag, num))
    return num


with open('input.txt') as f:
    data = f.read().split('\n')

rules={}
# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# faded blue bags contain no other bags.
#
# rules = {'light red': {'bright white': 1, 'muted yellow': 2}, 'dark orange': {'bright white': 3, 'muted yellow': 4}, 'faded blue': {}}
for d in data:
    k = d.split(' bags contain ')
    bag = k[0]
    contents = k[1]

    sub_bags = {}

    if not contents[0:2] == "no":
        clist = contents.split(',')
        for sub_bag in clist:
            d = sub_bag.strip().split(' ')
            bcount = d[0]
            btype = " ".join(d[1:-1])

            sub_bags[btype] = int(bcount)
    
    rules[bag] = sub_bags

print('\n\nAnswer is {}'.format(num_bags("", rules, 'shiny gold')))
