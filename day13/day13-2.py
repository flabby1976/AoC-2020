with open('input.txt') as f:
    notes = [d for d in f.read().split('\n')]

bus_notes = [d for d in notes[1].split(',')]
bus_ids = [int(d) for d in bus_notes if not d == "x"]

# These are the departure time offsets required
offsets = [bus_notes.index(str(d)) % d for d in bus_ids]

# Consider each bus in order of their journey time (shortest first)
key = [i[0] for i in sorted(enumerate(bus_ids), key=lambda x:x[1])]

timestamp = 0

# start by steping one timestep at a time
step = 1

for i in key:

    print(step)

    Found = False
    while True:

        timestamp += step
        wait_times = [(int(d) - timestamp % int(d)) % int(d) for d in bus_ids]

        if not Found:
            print(wait_times)

        if wait_times[i] == offsets[i]:
            if not Found:
                Found = True
                T1 = timestamp
            else:
                # Measure number of timesteps for this to repeat and set step to this for next bus
                # Using this means this and all prev bus wait times will stay the same
                step = timestamp - T1
                break

print(T1)