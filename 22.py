from parse_input import parse

def look_8_ways(y, x):
  directions = {
    'NW': (-1, -1),
    'N' : (-1,  0),
    'NE': (-1,  1),
    'E' : ( 0,  1),
    'SE': ( 1,  1),
    'S' : ( 1,  0),
    'SW': ( 1, -1),
    'W' : ( 0, -1)
  }
  adjacent_occupied = 0
  for direction in directions.values():
    if check_direction(y, x, direction):
      adjacent_occupied += 1
    # dir_y = y + direction[0]
    # dir_x = x + direction[1]
    # if dir_y >= 0 and dir_x >= 0:
    #   try:
    #     if seats_layout[dir_y][dir_x] == '#':
    #       adjacent_occupied += 1
    #   except IndexError:
    #     continue
    # if adjacent_occupied == 4:
    #   return 'L'
  return adjacent_occupied

def check_direction(y, x, direction):
  y += direction[0]
  x += direction[1]
  if y < 0 or x < 0:
    return False
  if y == len(seats_layout) or x == len(seats_layout[0]):
    return False
  if seats_layout[y][x] == 'L':
    return False
  if seats_layout[y][x] == '#':
    return True
  return check_direction(y, x, direction)


def simultate_round():
  global seats_layout
  global rounds
  rounds += 1
  print(rounds)
  for row in seats_layout:
    print(row)
  print()
  next_seats_layout = seats_layout.copy()

  for y, row in enumerate(seats_layout):
    next_row = ''
    for x, seat in enumerate(row):
      if seat != '.':
        adjacent_occupied = look_8_ways(y, x)
        if seat == 'L':
          if adjacent_occupied:
            next_row += 'L'
          else:
            next_row += '#'
        elif seat == '#':
          if adjacent_occupied < 5:
            next_row += '#'
          else:
            next_row += 'L'
      else:
        next_row += '.'
    
    next_seats_layout[y] = next_row

  if seats_layout != next_seats_layout:
    seats_layout = next_seats_layout
    simultate_round()

seats_layout = parse('21input.txt')

rounds = 0
simultate_round()

occupied = 0
for row in seats_layout:
  for seat in row:
    if seat == '#':
      occupied += 1
print(occupied)