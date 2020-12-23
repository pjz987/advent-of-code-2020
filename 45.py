import time
from generator_test import index_finder

cups = list('487912365')
# cups = list('389125467')
cups = [int(num) for num in cups]
# cups.extend(range(max(cups), 1000001))

start_to_pre_while = 0
pre_while_to_pre_index = 0
pre_index_to_end = 0

def turn(cups):
  global start_to_pre_while
  global pre_while_to_pre_index
  global pre_index_to_end
  start = time.time()

  current_cup = cups[0]
  three_cups = cups[1:4]
  destination_cup = current_cup - 1

  pre_while = time.time()
  start_to_pre_while += pre_while - start

  while destination_cup in three_cups or destination_cup == 0:
    destination_cup -= 1
    if destination_cup < min(cups):
      destination_cup = max(cups)

  pre_index = time.time()
  pre_while_to_pre_index += pre_index - pre_while

  remaining_cups = cups[4:]

  # destination_cup_index = remaining_cups.index(destination_cup)
  destination_cup_index = next(index_finder(remaining_cups, destination_cup))
  new_cups = remaining_cups[:destination_cup_index + 1] + three_cups + remaining_cups[destination_cup_index + 1:] + [current_cup]

  end = time.time()
  pre_index_to_end += end - pre_index

  return new_cups


def final_answer(cups):
  one_i = cups.index(1)
  return cups[(one_i + 1) % len(cups)] * cups[(one_i + 2) % len(cups)]

then = time.time()

turns = 10
for i in range(turns):
  if i % 100 == 0:
    now = time.time()
    print()
    print(i)
    print(now - then)
    then = now
  cups = turn(cups)

print('start_to_pre_while', start_to_pre_while / turns)
print('pre_while_to_pre_index', pre_while_to_pre_index / turns)
print('pre_index_to_end', pre_index_to_end / turns)

print(cups)