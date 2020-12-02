from parse_input import parse

def check_line(line):
  line = line.split()
  occurence_positions = [int(num) -1 for num in line[0].split('-')]
  letter = line[1].strip(':')
  password = line[2]
  valid = False
  for position in occurence_positions:
    if password[position] == letter:
      valid = not valid
  return valid

input_list = parse('03input.txt')

count = 0
for line in input_list:
  if check_line(line):
    count += 1

print(count)
