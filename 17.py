from parse_input import parse4

XMAS = parse4('17input.txt')

def find_invalid_num(index):
  global XMAS
  current_num = XMAS[index]
  preamble = XMAS[index - 25:index]
  for i, x in enumerate(preamble):
    for j, y in enumerate(preamble):
      if i != j:
        if x + y == current_num:
          index += 1
          return find_invalid_num(index)
  return current_num, index

print(find_invalid_num(25))