from parse_input import parse

boot_code = parse('15input.txt')

acc = 0
line_no = 0
lines_visited = []

def boot(line_no):
  global boot_code
  global acc
  if line_no in lines_visited:
    return acc
  lines_visited.append(line_no)

  line = boot_code[line_no]
  cmd = line.split(' ')[0]
  val = int(line.split(' ')[1])#[1:])
  # sign = line.split(' ')[1][0]
  # print(cmd, val)

  if cmd == 'acc':
    acc += val
    line_no += 1
  elif cmd == 'jmp':
    line_no += val
  elif cmd == 'nop':
    line_no += 1
  
  return boot(line_no)
  
print(boot(0))