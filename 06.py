from parse_input import parse
import sys
sys.setrecursionlimit(1500)

tree_map = parse('05input.txt')
slopes = [
  {'x': 1, 'y': 1},
  {'x': 3, 'y': 1},
  {'x': 5, 'y': 1},
  {'x': 7, 'y': 1},
  {'x': 1, 'y': 2},
]
coordinates = {
  'x': 0,
  'y': 0
}

def make_move(tree_map, coordinates, slopes, slope_count=0, tree_count=0, mult_total=1):
  row = tree_map[coordinates['y']]
  slope = slopes[slope_count]
  if row[coordinates['x'] % len(row)] == '#':
    tree_count += 1
  coordinates['x'] += slope['x']
  coordinates['y'] += slope['y']
  if coordinates['y'] >= len(tree_map):
    mult_total *= tree_count
    slope_count += 1
    if slope_count == len(slopes):
      return mult_total
    coordinates = {'x': 0, 'y': 0}
    return make_move(tree_map, coordinates, slopes, slope_count=slope_count, mult_total=mult_total)
  return(make_move(tree_map, coordinates, slopes, slope_count=slope_count, tree_count=tree_count, mult_total=mult_total))


# line = tree_map[coordinates['y']]
# print(line, len(line))
print(make_move(tree_map, coordinates, slopes))