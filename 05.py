from parse_input import parse

tree_map = parse('05input.txt')
coordinates = {
  'x': 0,
  'y': 0
}

def make_move(tree_map, coordinates, tree_count = 0):
  row = tree_map[coordinates['y']]
  if row[coordinates['x'] % len(row)] == '#':
    tree_count += 1
  coordinates['x'] += 3
  coordinates['y'] += 1
  if coordinates['y'] == len(tree_map):
    return tree_count
  return(make_move(tree_map, coordinates, tree_count))


# line = tree_map[coordinates['y']]
# print(line, len(line))
print(make_move(tree_map, coordinates))