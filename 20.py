from parse_input import parse_sort
import time
time
# import sys
# sys.setrecursionlimit(10001)

adapters = parse_sort('19input.txt')
adapters.append(0)
adapters.append(max(adapters) + 3)
adapters.sort()

# arrangements = []
arrangements = 0
arrangement_stack = []
# iterations = 0
time_start = time.time()
def find_arrangements(arrangement=[], i=0):
  # global iterations
  # iterations += 1
  # print(iterations)
  global adapters
  global arrangement_stack
  global arrangements
  arrangement = arrangement.copy()
  adapter_i = adapters[i]
  arrangement.append(adapter_i)
  next_3 = [adapter for adapter in adapters[i+1:i+4] if adapter <= adapter_i + 3]
  arrangement_stack.append(arrangement)

  for adapter in next_3:
    index = adapters.index(adapter)
    find_arrangements(arrangement, index)
    # arrangement_stack.pop()
    
  if i == len(adapters) - 1:
    arrangements += 1
    # arrangements.append(tuple(arrangement))
    # arrangement_stack.pop()
  
  arrangement_stack.pop()
  
find_arrangements()
time_end = time.time()
print(arrangements)
time_set = time.time()
print(time_set-time_end)
print(time_end-time_start)