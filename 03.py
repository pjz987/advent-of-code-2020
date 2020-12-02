from parse_input import parse

def check_line(line):
  line = line.split()
  count_range = line[0].split('-')
  letter = line[1].strip(':')
  password = line[2]
  letter_count = 0
  for char in password:
    if letter == char:
      letter_count += 1
  if letter_count >= int(count_range[0]) and letter_count <= int(count_range[1]):
    return True

input_list = parse('03input.txt')

count = 0
for line in input_list:
  if check_line(line):
    count += 1

print(count)
