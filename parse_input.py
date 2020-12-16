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
    lines = [line.split() for line in lines if line !='\n']
    return lines

def parse3(path):
  with open(path, 'r') as raw:
    lines = raw.read().split('\n\n')
    lines = [line for line in lines if line]
    return lines
  
def parse4(path):
  with open(path, 'r') as raw:
    lines = raw.readlines()
  input_list = []
  for line in lines:
    if line != '\n':
      input_list.append(int(line))
  return input_list

def parse_sort(path):
  with open(path, 'r') as raw:
    lines = raw.readlines()
  input_list = []
  for line in lines:
    if line != '\n':
      input_list.append(int(line))
  input_list.sort()
  return input_list

def parse_2d_array(path):
  with open(path, 'r') as raw:
    lines = raw.readlines()
  input_list = []
  for line in lines:
    if line != '\n':
      input_list.append(list(line.strip()))
  return input_list

def parse_newlines(path):
  with open(path, 'r') as raw:
    full_file = raw.read()
  input_list = full_file.split('\n\n')
  # if input_list[-1] == '\n':
  input_list.pop()
  return input_list