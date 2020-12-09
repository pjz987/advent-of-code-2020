from parse_input import parse4

XMAS = parse4('17input.txt')

def find_invalid_num(index):
  global XMAS
  current_num = XMAS[index]
  preamble = XMAS[index - 25:index] # 5 - 25
  for i, x in enumerate(preamble):
    for j, y in enumerate(preamble):
      if i != j:
        if x + y == current_num:
          index += 1
          return find_invalid_num(index)
  return current_num, index

def get_encryption_weakness(index):
  global XMAS
  global invalid_num
  global invalid_num_index

  XMAS_subset = XMAS[index:invalid_num_index]
  # print(XMAS_subset)
  for i in range(len(XMAS_subset)):
    for j in range(len(XMAS_subset)):
      sum_range = sum(XMAS_subset[i:j])
      if sum_range == invalid_num:
        return min(XMAS_subset[i:j]) + max(XMAS_subset[i:j])
  index += 1
  return get_encryption_weakness(index)


invalid_num, invalid_num_index = find_invalid_num(25) # 5 - 25
print(get_encryption_weakness(0))