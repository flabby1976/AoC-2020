def valid_value_for_field(field, value):
    return any([value in range(r[0], r[1]+1) for r in fields[field]])

def valid_value(fields, value):
    return any([valid_value_for_field(field, value) for field, valid_ranges in fields.items()])

with open('input.txt') as f:
    input = [d for d in f.read().split('\n\n')]

fields_string = input[0]
my_ticket_string = input[1]
nearby_tickets_string = input[2]

fields = {d.split(": ")[0]: d.split(": ")[1].split(" or ") for d in fields_string.split("\n")}
fields = {name: [(int(r.split("-")[0]), int(r.split("-")[1])) for r in ranges] for name, ranges in fields.items()}
my_ticket = [int(d) for d in my_ticket_string.split("\n")[1].split(",")]
nearby_tickets = [[int(i) for i in d.split(",")] for d in nearby_tickets_string.split("\n")[1:]]

valid_nearby_tickets = [ticket for ticket in nearby_tickets if not any([not valid_value(fields, value) for value in ticket])]

# A list of all options for the feild associated with each ticket char position
options = [list(fields.keys()) for i in my_ticket]

#step though every postion on the ticket
for i in range(len(my_ticket)):
    #make a list of all the fields that can't be at this position
    invalid = []

    # step though all the remaining valid field options for this position
    for cl in options[i]:

        # look through all the valid tickets and check if any of them violate the rule for this field
        # if so add the field to the list of invalid fields for this position
        for ticket in valid_nearby_tickets:
            if not valid_value_for_field(cl, ticket[i]):
                invalid.append(cl)
                break
    
    # Remove the invalid fields from the options for this position
    for cl in invalid:
        options[i].remove(cl)

# Should be at least one position with only only valid field.
# find it, trim it from the other positions and repeat
ans={}
while True:
    found = None
    for n, o in enumerate(options):
        if len(o)==1:
            ans[o[0]] = n+1
            found = o[0]
            break
    if found:
        for o in options:
            if found in o:
                o.remove(found)
    else:
        break

print("\n")
print(ans)

# calculate the answer
a=1
for key, value in ans.items():
    if "departure" in key:
        a = a * my_ticket[value-1]


print(a)







