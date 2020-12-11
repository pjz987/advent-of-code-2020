from parse_input import parse

def check_empty(y, x, row):
  for y_adj in range(y - 1, y + 2):
    if y_adj >= 0 and y_adj < len(seats_layout):
      for x_adj in range(x - 1, x + 2):
        if x_adj >= 0 and x_adj < len(row):
          if y_adj != x_adj:
            if seats_layout[y_adj][x_adj] == '#':
              return 'L', 0
  return '#', 1

def check_occupied(y, x, row):
  adjacent_occupied = 0
  for y_adj in range(y - 1, y + 2):
    if y_adj >= 0 and y_adj < len(seats_layout):
      for x_adj in range(x - 1, x + 2):
        if x_adj >= 0 and x_adj < len(row):
          if y_adj != y and x_adj != x:
            if seats_layout[y_adj][x_adj] == '#':
              adjacent_occupied += 1
  if adjacent_occupied >= 4:
    return 'L', -1
  return '#', 0

def look_8_ways(y, x):
  directions = [
    (-1, -1),
    (-1,  0),
    (-1,  1),
    ( 0, -1),
    ( 0,  1),
    ( 1, -1),
    ( 1,  0),
    ( 1,  1)
  ]
  adjacent_occupied  = 0
  for direction in directions:
    dir_y = y + direction[0]
    dir_x = x + direction[1]
    if dir_y >= 0 and dir_x >= 0:
      try:
        if seats_layout[dir_y][dir_x] == '#':
          adjacent_occupied += 1
      except IndexError:
        continue
    # if adjacent_occupied == 4:
    #   return 'L'
  return adjacent_occupied


def simultate_round():
  global rounds
  global seats_layout
  rounds += 1
  next_seats_layout = seats_layout.copy()
  change = False

  for y, row in enumerate(seats_layout):
    next_row = ''
    # row_copy = row.copy()
    for x, seat in enumerate(row):
      if seat != '.':
        adjacent_occupied = look_8_ways(y, x)
        if seat == 'L':
          if adjacent_occupied:
            next_row += 'L'
          else:
            next_row += '#'
        elif seat == '#':
          if adjacent_occupied < 4:
            next_row += '#'
          else:
            next_row += 'L'
      else:
        next_row += '.'
      # if seat == 'L':
      #   next_seat, difference = check_empty(y, x, row)
      #   next_row += next_seat
      #   occupied += difference
      #   if change == False and difference:
      #     change = True

      # elif seat == '#':
      #   next_seat, difference = check_occupied(y, x, row)
      #   next_row += next_seat
      #   occupied += difference
      #   if change == False and difference:
      #     change = True
      
      # else:
      #   next_row += '.'
    
    next_seats_layout[y] = next_row

  for row in seats_layout:
    print(row)
  print()
  # if rounds > 10:
  #   return
  # if change == False:
  #   return occupied

  if seats_layout != next_seats_layout:
    seats_layout = next_seats_layout
    simultate_round()

rounds = 0
seats_layout = parse('21input.txt')

print(simultate_round())

print(rounds)

occupied = 0
for row in seats_layout:
  for seat in row:
    if seat == '#':
      occupied += 1
print(occupied)