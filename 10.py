from parse_input import parse
from math import floor, ceil

# test_row = 'FBFBBFF'
def decode_row(bsp_row, row_range=(0, 127)):
  f_or_b = bsp_row[0]
  bsp_row = bsp_row[1:]
  low = row_range[0]
  high = row_range[1]
  middle = low + (high - low) / 2
  row_range = (low, floor(middle)) if f_or_b == 'F' else (ceil(middle), high)
  if bsp_row:
    return decode_row(bsp_row, row_range)
  return row_range[0]
# print(decode_row(test_row))

# test_column = 'RLR'
def decode_column(bsp_column, column_range=(0, 7)):
  l_or_r = bsp_column[0]
  bsp_column = bsp_column[1:]
  low = column_range[0]
  high = column_range[1]
  middle = low + (high - low) / 2
  column_range = (low, floor(middle)) if l_or_r == 'L' else (ceil(middle), high)
  if bsp_column:
    return decode_column(bsp_column, column_range)
  return column_range[0]
# print(decode_column(test_column))

boarding_passes = parse('09input.txt')
seat_ids = list(range(1024))

for boarding_pass in boarding_passes:
  # bsp = binary space partitioning
  bsp_row = boarding_pass[:7]
  bsp_column = boarding_pass[7:]
  row = decode_row(bsp_row)
  column = decode_column(bsp_column)
  seat_id = row * 8 + column
  seat_ids.remove(seat_id)

for seat_id in seat_ids:
  print(seat_id)

