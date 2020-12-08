with open('input.txt') as f:
    data = [d.split() for d in f.read().split('\n\n')]

print(data)

print('Number of groups: {}'.format(len(data)))

p = 0
for group in data:
    print('\nPeople in this group: {}'.format(len(group)))
    answer_set = set(group[0])
    for person in group:
        k = set(person)
        answer_set = answer_set.intersection(k)
    print('Group answer set: {}'.format(answer_set))
    print('Group answer set len: {}'.format(len(answer_set)))
    p = p + len(answer_set)

print('\n\nSum of all group answer set lengths: {}'.format(p))
