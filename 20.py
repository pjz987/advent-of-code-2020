from parse_input import parse_sort
# import time

adapters = parse_sort('19input.txt')
adapters.append(0)
adapters.append(max(adapters) + 3)
adapters.sort()

blocks = []

start_block_i = 0

def find_arrangements(i=0):
  global arrangements
  global block

  adapter_i = block[i]
  next_3 = block[i + 1:i + 4]

  for j, adapter in enumerate(next_3):
    if adapter <= adapter_i + 3:
      find_arrangements(i + j + 1)

  if i == len(block) - 1:
    arrangements += 1
    
for i, adapter in enumerate(adapters):
  if i == len(adapters) - 1:
    break
  if adapter + 3 == adapters[i + 1]:
    blocks.append(adapters[start_block_i:i+1])
    start_block_i = i + 1
# print(blocks)
answer = 1
for block in blocks:
  arrangements = 0
  find_arrangements(0)
  answer *= arrangements
  print(len(block), arrangements, answer)
  print(block)
print(answer)



























# arrangements = 0
# mult_count = 0
# from_to = []
# to_from = []
# jolt_dict = {}
# i_dict = {}








  # if i == len(adapters) - 1:
  #   break
#   jolt_dict[adapter] = []
#   i_dict[i] = []
#   for j, next_adapter in enumerate(adapters[i+1:i+4]):
#     if next_adapter <= adapter + 3:
#       to_from.append((next_adapter, adapter))
#       from_to.append((adapter, next_adapter))
#       jolt_dict[adapter].append(next_adapter)
#       i_dict[i].append(j + 1)

# print(i_dict)
# for key, value in i_dict.items():
#   print(key, value)

# print(jolt_dict)
# for key, value in jolt_dict.items():
#   print(key, value)

# print(len(from_to))
# print(to_from)
# time_start = time.time()
  
# find_arrangements()
# print(arrangements)

# time_end = time.time()
# print(time_end-time_start)