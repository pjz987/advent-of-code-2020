from parse_input import parse

notes = parse('25input.txt')
# print(notes)

timestamp = int(notes[0])
bus_ids = [int(bus_id) for bus_id in notes[1].split(',') if bus_id != 'x']

# print(timestamp)
# print(bus_ids)
next_bus_tups = []
for bus_id in bus_ids:
  time = 0
  while time <= timestamp:
    time += bus_id
  next_bus_tups.append((time, bus_id))

earliest_time = min([next_bus_tup[0] for next_bus_tup in next_bus_tups])

for next_bus_tup in next_bus_tups:
  if next_bus_tup[0] == earliest_time:
    next_bus_id = next_bus_tup[1]

print(next_bus_id * (earliest_time - timestamp))