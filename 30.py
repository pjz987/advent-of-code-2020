import time
from collections import defaultdict

def give_none():
  return None

dd = defaultdict(give_none)

numbers = [5, 2, 8, 16, 18, 0, 1]
# numbers = [0, 3, 6]

# numbers_dict = {}
for i, num in enumerate(numbers):
  if dd[num] is None:
    dd[num] = (None, i)

  # if num not in numbers_dict.keys():
  #   numbers_dict[num] = (None, i)

start = time.time()
now = time.time()
try:
  while len(numbers) < 30000000:
    if len(numbers) == 29999999: # % 10000 == 0: # or len(numbers) == 2019:
      then = now
      now = time.time()
      print('length    ', len(numbers))
      print('time      ', now - then)
      print('full time ', now - start)
      print()

    # prev_num = numbers[-2]
    
    # numbers_dict[prev_num] = len(numbers) - 2

    last_num = numbers[-1]

    # if last_num in numbers[:-1]:
    if dd[last_num][0] is not None:
      numbers.append(dd[last_num][1] - dd[last_num][0])
      # numbers.append(numbers_dict[last_num][1] - numbers_dict[last_num][0])

    else:
      # numbers_dict[0] = len(numbers)
      numbers.append(0)
    
    new_num = numbers[-1]
    # try:
    #   numbers_dict[numbers[-1]] = (numbers_dict[numbers[-1]][1], len(numbers) - 1)
    # except(KeyError):
    #   numbers_dict[new_num] = (None, len(numbers) - 1)

    if dd[new_num] is None:
      dd[new_num] = (None, len(numbers) - 1)
    else:
      dd[new_num] = (dd[numbers[-1]][1], len(numbers) - 1)

    # if new_num not in numbers_dict.keys():
    #   numbers_dict[new_num] = (None, len(numbers) - 1)
    # else:
    #   numbers_dict[numbers[-1]] = (numbers_dict[numbers[-1]][1], len(numbers) - 1)
    
    

except(KeyboardInterrupt):
  print(len(numbers))

print(numbers[-1])