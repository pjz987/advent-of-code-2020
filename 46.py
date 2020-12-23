cups = list('487912365')
# cups = list('389125467')
cups = [int(num) for num in cups]
print(cups)

def turn(cups):
  current_cup = cups[0]
  three_cups = cups[1:4]
  destination_cup = current_cup - 1

  while destination_cup in three_cups or destination_cup == 0:
    destination_cup -= 1
    if destination_cup < min(cups):
      destination_cup = max(cups)

  remaining_cups = cups[4:]
  new_cups = remaining_cups[:remaining_cups.index(destination_cup) + 1] + three_cups + remaining_cups[remaining_cups.index(destination_cup) + 1:] + [current_cup]

  return new_cups

def final_order(cups):
  one_i = cups.index(1)
  return ''.join([str(num) for num in (cups[one_i + 1:] + cups[:one_i])])


for _ in range(100):
  cups = turn(cups)

print(final_order(cups))