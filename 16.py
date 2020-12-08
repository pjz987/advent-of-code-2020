from parse_input import parse

boot_code = parse('15input.txt')

acc = 0
line_no = 0
lines_visited = []

def boot(line_no):
  global boot_code
  global acc
  if line_no in lines_visited:
    return False
  if line_no == len(boot_code) - 1:
    return True
  lines_visited.append(line_no)

  line = boot_code[line_no]
  cmd = line.split(' ')[0]
  val = int(line.split(' ')[1])#[1:])

  if cmd == 'acc':
    acc += val
    line_no += 1
  elif cmd == 'jmp':
    line_no += val
  elif cmd == 'nop':
    line_no += 1
  
  return boot(line_no)

for i, line in enumerate(boot_code):
  changed = False
  changed_to = ''
  cmd = line.split(' ')[0]

  if cmd == 'jmp':
    boot_code[i] = line.replace('jmp', 'nop')
    changed = True
    changed_to = 'nop'
  elif cmd == 'nop':
    boot_code[i] = line.replace('nop', 'jmp')
    changed = True
    changed_to = 'jmp'

  if changed:
    acc = 0
    lines_visited = []
    if boot(0):
      print(acc)
      break
    else:
      boot_code[i] = line

  

# print(boot(0))