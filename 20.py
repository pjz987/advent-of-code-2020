from parse_input import parse_sort
import time

adapters = parse_sort('19input.txt')
adapters.append(0)
adapters.append(max(adapters) + 3)
adapters.sort()

# arrangements = []
arrangements = 0
# arrangement_stack = []
# iterations = 0
time_start = time.time()
def find_arrangements(i=0):
  global arrangements
  global adapters
  # print(arrangements)
  adapter_i = adapters[i]
  next_3 = adapters[i + 1:i + 4]

  for j, adapter in enumerate(next_3):
    if adapter <= adapter_i + 3:
      find_arrangements(i + j + 1)

  if i == len(adapters) - 1:
    arrangements += 1
  
find_arrangements()
time_end = time.time()
print(arrangements)
time_set = time.time()
print(time_set-time_end)
print(time_end-time_start)