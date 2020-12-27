import copy

with open('input.txt') as f:
    rules, messages = f.read().split('\n\n')

rule_strings = [rule for rule in rules.split('\n')]
messages = messages.split('\n')

rules={}
for rule in rule_strings:
    num,code = rule.split(': ')
    rules[num] = code

# print(rules)

map_list=[]
map_list.append(rules['0'])
del rules['0']
print(map_list)

def replace_d(map_list, n, rep):
    new_map=[]
    n=str(j)
    print('Trying rule {} -> {}'.format(n,rep))
    for i in map_list:
        if n in i.split(' '):
            for k in rep.split(' | '):
                    new_map.append(i.replace(n,k).replace('"',''))
        else:
            new_map.append(i)
    return new_map

for _ in range(10):
    for j in range(1,len(rules)+1):
        new_map = replace_d(map_list, j, rules[str(j)])                
        map_list = new_map
   
    # print(new_map)
    print(len(new_map))
    input('Paused ..')

new_map = [d.replace(' ','') for d in new_map]


ans=0
for d in messages.split('\n'):
    print(d)
    if d in new_map:
        print("YES")
        ans+=1

print(ans)

