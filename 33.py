from parse_input import parse_string
from copy import deepcopy

input = parse_string('33input.txt')
plane = [list(row) for row in input.split('\n')]

dimension = [plane]

def pad_dimension(dimension):
  new_value = len(dimension[0][0])
  new_plane_string = (('.' * new_value + '\n') * new_value).strip('\n')
  new_plane = [list(row) for row in new_plane_string.split('\n')]
  new_plane_copy = deepcopy(new_plane)
  dimension.insert(0, new_plane)
  dimension.append(new_plane_copy)

  for plane in dimension:
    plane.insert(0, list('.' * new_value))
    plane.append(list('.' * new_value))

  for plane in dimension:
    for row in plane:
      row.insert(0, '.')
      row.append('.')
  
  return dimension


def get_next_dimension(dimension):
  next_dimension = deepcopy(dimension)
  for i, z_plane in enumerate(dimension):
    for j, y_row in enumerate(z_plane):
      for k, x_cell in enumerate(y_row):

        z_start = 0 if i == 0 else -1
        z_end = 1 if i == len(dimension) - 1 else 2
        y_start = 0 if j == 0 else -1
        y_end = 1 if j == len(z_plane) - 1 else 2
        x_start = 0 if k == 0 else -1
        x_end = 1 if k == len(y_row) - 1 else 2

        active_neighbors = 0

        for z in range(z_start, z_end):
          for y in range(y_start, y_end):
            for x in range(x_start, x_end):
              if z != 0 or y != 0 or x != 0:
                try:
                  if dimension[i + z][j + y][k + x] == '#':
                    active_neighbors += 1
                except(IndexError):
                  print()
                  print(len(dimension))
                  print(len(z_plane))
                  print(len(y_row))
                  # print(y, z, x)
                  print(i + y, j + z, k + x)

        if x_cell == '#':
          if active_neighbors == 2 or active_neighbors == 3:
            next_x_cell = '#'
          else:
            next_x_cell = '.'
        else:
          if active_neighbors == 3:
            next_x_cell = '#'
          else:
            next_x_cell = '.'
        
        next_dimension[i][j][k] = next_x_cell

  return next_dimension

for _ in range(6):
  # for plane in dimension:
  #   print()
  #   for row in plane:
  #     print(row)
  dimension = pad_dimension(dimension)
  # for plane in dimension:
  #   print()
  #   for row in plane:
  #     print(row)
  dimension = get_next_dimension(dimension)
  # for plane in dimension:
  #   print()
  #   for row in plane:
  #     print(row)

count_active = 0
for plane in dimension:
  for row in plane:
    for cell in row:
      if cell == '#':
        count_active += 1
print(count_active)
