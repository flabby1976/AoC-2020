def valid_value(fields, value):
    return any([value in range(r[0], r[1]+1) for field, valid_ranges in fields.items() for r in valid_ranges])

with open('input.txt') as f:
    input = [d for d in f.read().split('\n\n')]

fields_string = input[0]
my_ticket_string = input[1]
nearby_tickets_string = input[2]

fields = {d.split(": ")[0]: d.split(": ")[1].split(" or ") for d in fields_string.split("\n")}
fields = {name: [(int(r.split("-")[0]), int(r.split("-")[1])) for r in ranges] for name, ranges in fields.items()}

my_ticket = my_ticket_string.split("\n")[1].split(",")
nearby_tickets = [[int(i) for i in d.split(",")] for d in nearby_tickets_string.split("\n")[1:]]

invalid_values=[value for ticket in nearby_tickets for value in ticket if not valid_value(fields, value)]
print(invalid_values, sum(invalid_values))