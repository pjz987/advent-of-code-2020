from parse_input import parse
import sys
# sys.setrecursionlimit(100000)

notes = parse('25input.txt')
notes[1] = '17,x,13,19' # test
# # notes[1] = '13,19' # test
# notes[1] = '67,7,59,61'

bus_ids = [int(bus_id) if bus_id != 'x' else bus_id for bus_id in notes[1].split(',')]

def find_contiguous_bus_times(time=0):
  global bus_ids
  count = time
  for bus_id in bus_ids:
    if bus_id == 'x':
      count += 1
      continue
    if bus_id != 'x':
      if count % bus_id:
        return find_contiguous_bus_times(time + bus_ids[0])
      else:
        count += 1
  for i, bus_id in enumerate(bus_ids):
    continue
    # print('i', i)
    # if bus_id == 'x':
    #   print('x')
    # else:
    #   print(count, bus_id)
      # print(count % bus_id)
  return time, i, bus_id

ranges = []
nums = []
for i, bus_id in enumerate(bus_ids):
  if bus_id != 'x':
    nums.append(bus_id)
  if i < len(bus_ids) - 1 and bus_id != 'x':
    id_range = [bus_id]
    for bus_id in bus_ids[i + 1:]:
      id_range.append(bus_id)
      if bus_id != 'x':
        break
    ranges.append(id_range)
for id_range in ranges:
  bus_ids = id_range
  print(find_contiguous_bus_times())
  print(id_range)

# product = 1
# for num in nums:
#   product *= num
#   print(product)
# print(product - len(bus_ids))

# for i, bus_id_key in enumerate(bus_ids):
#   if bus_id_key != 'x':
#     sub_list = bus_ids[i:]
#     for j, bus_id_value in enumerate(sub_list):
#       if j == 0 or bus_id_value == 'x':
#         continue
#       bus_ids = sub_list[:j + 1]
#       print('bus_id_key', bus_id_key)
#       # print('time', find_contiguous_bus_times())
#       time, offset, next_bus = find_contiguous_bus_times()
#       bus_id_dict[bus_id_key] = {
#         'time': time,
#         'offset': offset,
#         'next_bus': next_bus
#       }
#       # print(bus_id_dict)

# print(bus_id_dict)
