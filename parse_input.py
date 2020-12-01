def parse(path):
  with open(path, 'r') as raw:
    lines = raw.readlines()
  
  input_list = []
  for line in lines:
    if line != '\n':
      input_list.append(int(line.strip()))
  return input_list