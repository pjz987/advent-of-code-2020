def parse(path):
  with open(path, 'r') as raw:
    lines = raw.readlines()
  
  input_list = []
  for line in lines:
    if line != '\n':
      input_list.append(line.strip())
  return input_list

def parse2(path):
  with open(path, 'r') as raw:
    lines = raw.read().split('\n\n')
    lines = [line.split() for line in lines]
    return lines