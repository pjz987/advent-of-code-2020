from parse_input import parse_string
from copy import deepcopy

input = parse_string('33input.txt')
plane = [list(row) for row in input.split('\n')]

dimension = [[plane]]

def pad_dimension(dimension):
  new_value = len(dimension[0][0][0])
  new_plane_string = (('.' * new_value + '\n') * new_value).strip('\n')
  new_plane = [list(row) for row in new_plane_string.split('\n')]

  new_box = deepcopy(dimension[0])
  # print()
  # print('new_box')
  # print(new_box)

  for i, plane in enumerate(dimension[0]):
    for j, row in enumerate(plane):
      for k, cell in enumerate(row):
        # print()
        # print('plane')
        # print(plane)
        # print('row')
        # print(row)
        # print('cell')
        # print(cell)
        new_box[i][j][k] = '.'
  
  new_box_copy = deepcopy(new_box)

  dimension.insert(0, new_box)
  dimension.append(new_box_copy)

  for box in dimension:
    new_plane_copy1 = deepcopy(new_plane)
    box.insert(0, new_plane_copy1)
    new_plane_copy2 = deepcopy(new_plane)
    box.append(new_plane_copy2)

    for plane in box:
      plane.insert(0, list('.' * new_value))
      plane.append(list('.' * new_value))

      for row in plane:
        row.insert(0, '.')
        row.append('.')
  
  return dimension


def get_next_dimension(dimension):
  next_dimension = deepcopy(dimension)
  for i, w_box in enumerate(dimension):
    for j, z_plane in enumerate(w_box):
      for k, y_row in enumerate(z_plane):
        for l, x_cell in enumerate(y_row):

          w_start = 0 if i == 0 else -1
          w_end = 0 if i == len(dimension) - 1 else 2
          z_start = 0 if j == 0 else -1
          z_end = 1 if j == len(w_box) - 1 else 2
          y_start = 0 if k == 0 else -1
          y_end = 1 if k == len(z_plane) - 1 else 2
          x_start = 0 if l == 0 else -1
          x_end = 1 if l == len(y_row) - 1 else 2

          active_neighbors = 0

          for w in range(w_start, w_end):
            for z in range(z_start, z_end):
              for y in range(y_start, y_end):
                for x in range(x_start, x_end):
                  if w !=0 or z != 0 or y != 0 or x != 0:
                    try:
                      if dimension[i + w][j + z][k + y][l + x] == '#':
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
          
          next_dimension[i][j][k][l] = next_x_cell

  return next_dimension

for _ in range(6):
  # for box in dimension:
  #   print()
  #   for plane in box:
  #     print()
  #     for row in plane:
  #       print(row)
  dimension = pad_dimension(dimension)
  # for box in dimension:
  #   print()
  #   for plane in box:
  #     print()
  #     for row in plane:
  #       print(row)
  dimension = get_next_dimension(dimension)
  # for plane in dimension:
  #   print()
  #   for row in plane:
  #     print(row)

count_active = 0
for box in dimension:
  for plane in box:
    for row in plane:
      for cell in row:
        if cell == '#':
          count_active += 1
print(count_active)
