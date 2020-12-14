with open('input.txt') as f:
    notes = [d for d in f.read().split('\n')]

earliest_time = int(notes[0])
bus_ids = [d for d in notes[1].split(',') if not d == "x"]

wait_times = [int(d) - earliest_time % int(d) for d in bus_ids]
min_wait = min(wait_times)
best_bus = bus_ids[wait_times.index(min_wait)]

print(min_wait)
print(best_bus)
print(int(best_bus)*min_wait)