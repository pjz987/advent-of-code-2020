from parse_input import parse_newlines
from random import shuffle

class FullTile:
  def __init__(self, raw, x, x_offset, y, y_offset, history):
    self.x = x + x_offset
    self.y = abs(y + y_offset - 11)
    rows = raw.split('\n')
    self.id = rows[0].strip('Tile :')
    grid = rows[2:-1]
    for i, row in enumerate(grid):
      grid[i] = row[1:-1]
    self.grid = grid
    for transformation in history:
      if transformation == 'flip_h':
        self.flip_h()
      elif transformation == 'flip_v':
        self.flip_v()
      elif transformation == 'rotate':
        self.rotate()
  
  def flip_h(self):
    for i, row in enumerate(self.grid):
      self.grid[i] = row[::-1]
  
  def flip_v(self):
    self.grid = self.grid[::-1]
  
  def rotate(self):
    rotator = list(zip(*self.grid[::-1]))
    for i, row in enumerate(rotator):
      self.grid[i] == ''.join(row)
  
  def __repr__(self):
    return f"""
      id: {self.id}
      x: {str(self.x)} y: {str(self.y)}
      {str(self.grid)}
    """


class Tile:
  global tiles
  global defined_tiles
  def __init__(self, raw):
    self.x = None
    self.y = None
    rows = raw.split('\n')
    self.id = rows[0].strip('Tile :')
    rows = rows[1:]
    self.top = rows[0]
    self.bottom = rows[-1]
    self.left = ''
    self.right = ''
    for row in rows:
      self.left += row[0]
      self.right += row[-1]
    self.sides = self.get_sides_list()
    self.dict = self.get_sides_dict()
    self.top_neighbor = False
    self.right_neighbor = False
    self.bottom_neighbor = False
    self.left_neighbor = False
    self.history = []

  def get_neighbors(self):
    return [self.top_neighbor, self.right_neighbor, self.bottom_neighbor, self.left_neighbor]
  
  def get_sides_list(self):
    return [self.top, self.right, self.bottom, self.left]
  
  def get_sides_dict(self):
    return {'top': self.top, 'right': self.right, 'bottom': self.bottom, 'left': self.left}
  
  def rotate(self):
    top = self.top
    right = self.right
    bottom = self.bottom
    left = self.left
    self.top = left[::-1]
    self.right = top
    self.bottom = right[::-1]
    self.left = bottom
    self.sides = self.get_sides_list()
    self.dict = self.get_sides_dict()
    self.history.append('rotate')

  def flip_h(self):
    left = self.left
    self.left = self.right
    self.right = left
    self.top = self.top[::-1]
    self.bottom = self.bottom[::-1]
    self.sides = self.get_sides_list()
    self.dict = self.get_sides_dict()
    self.history.append('flip_h')

  def flip_v(self):
    top = self.top
    self.top = self.bottom
    self.bottom = top
    self.left = self.left[::-1]
    self.right = self.right[::-1]
    self.sides = self.get_sides_list()
    self.dict = self.get_sides_dict()
    self.history.append('flip_v')

  def check_tile(self, tile):
    for self_key, self_side in self.dict.items():
      for comp_key, comp_side in tile.dict.items():
        if self_side == comp_side:
          self.check_side(tile, self_key, comp_key)
        elif self_side == comp_side[::-1]:
          self.check_side_reversed(tile, self_key, comp_key)

  def set_neighbors(self, tile, self_key):
    if self_key == 'top':
      self.top_neighbor = True
      tile.bottom_neighbor = True
    if self_key == 'right':
      self.right_neighbor = True
      tile.left_neighbor = True
    if self_key == 'bottom':
      self.bottom_neighbor = True
      tile.top_neighbor = True
    if self_key == 'left':
      self.left_neighbor = True
      tile.right_neighbor = True

  def check_side(self, tile, self_key, comp_key):
    if self_key == 'top':
      if comp_key == 'bottom':
        self.set_neighbors(tile, self_key)
        return tile.set_coordinates(self.x, self.y + 1)
      if comp_key == 'top':
        tile.flip_v()
        self.set_neighbors(tile, self_key)
        return tile.set_coordinates(self.x, self.y + 1)

    if self_key == 'right':
      if comp_key == 'left':
        self.set_neighbors(tile, self_key)
        return tile.set_coordinates(self.x + 1, self.y)
      if comp_key == 'right':
        tile.flip_h()
        self.set_neighbors(tile, self_key)
        return tile.set_coordinates(self.x + 1, self.y)
    
    if self_key == 'bottom':
      if comp_key == 'top':
        self.set_neighbors(tile, self_key)
        return tile.set_coordinates(self.x, self.y - 1)
      if comp_key == 'bottom':
        tile.flip_v()
        self.set_neighbors(tile, self_key)
        return tile.set_coordinates(self.x, self.y - 1)

    if self_key == 'left':
      if comp_key == 'right':
        self.set_neighbors(tile, self_key)
        return tile.set_coordinates(self.x - 1, self.y)
      if comp_key == 'left':
        tile.flip_h()
        self.set_neighbors(tile, self_key)
        return tile.set_coordinates(self.x - 1, self.y)
    
    tile.rotate()

  def check_side_reversed(self, tile, self_key, comp_key):
    if self_key in ['top', 'bottom'] and comp_key in ['top, bottom']:
      tile.flip_h()
      return self.check_tile(tile)
    if self_key in ['left', 'right'] and comp_key in ['left', 'right']:
      tile.flip_v()
      return self.check_tile(tile)
    
    tile.rotate()

  def set_coordinates(self, x, y):
    self.x = x
    self.y = y
    defined_tiles.append(self)

  def __repr__(self):
    l = self.left
    r = self.right
    return f"""
      Tile: {self.id}
      {self.top}
      {l[1]}        {r[1]}
      {l[2]}        {r[2]}
      {l[3]}        {r[3]}
      {l[4]}        {r[4]}
      {l[5]}        {r[5]}
      {l[6]}        {r[6]}
      {l[7]}        {r[7]}
      {l[8]}        {r[8]}
      {self.bottom}
    """

def grab_undefined_tile(tiles):
  for tile in tiles:
    if tile.x is None and tile.y is None:
      return tile

def grab_defined_tile(defined_tiles):
  for tile in defined_tiles:
    neighbors = [neighbor for neighbor in tile.get_neighbors() if neighbor]
    if len(neighbors) < 4:
      return tile

tiles_list = parse_newlines('39input.txt')
# for tile in tiles_list:
#   print(tile)
tiles = [Tile(tile) for tile in tiles_list]
defined_tiles = []
starting_tile = tiles[0]
starting_tile.set_coordinates(0, 0)

x_high = 0
x_low = 0
y_high = 0
y_low = 0

while len(defined_tiles) < len(tiles):
  shuffle_tiles = tiles[:]
  shuffle_defined_tiles = defined_tiles[:]
  shuffle(shuffle_tiles)
  shuffle(shuffle_defined_tiles)
  defined_tile = grab_defined_tile(shuffle_defined_tiles)
  undefined_tile = grab_undefined_tile(shuffle_tiles)
  defined_tile.check_tile(undefined_tile)

  if undefined_tile.x is not None and undefined_tile.y is not None:
    new_tile = undefined_tile
    x_high = new_tile.x if new_tile.x > x_high else x_high
    x_low = new_tile.x if new_tile.x < x_low else x_low
    y_high = new_tile.y if new_tile.y > y_high else y_high
    y_low = new_tile.y if new_tile.y < y_low else y_low

# corners = []
# for tile in defined_tiles:
#   if tile.x == x_high and tile.y in [y_high, y_low]:
#     corners.append(tile)
#   if tile.x == x_low and tile.y in [y_high, y_low]:
#     corners.append(tile)

# product = 1
# for tile in corners:
#   product *= int(tile.id)
# print(product)
# print(x_high + abs(x_low), x_low + abs(x_low))
# print(y_high + abs(y_low), y_low + abs(y_low))

full_tiles = [[None] * 12] * 12
for tile in tiles:
  for raw_tile in tiles_list:
    if tile.id in raw_tile:
      # print('here?')
      full_tile = FullTile(raw_tile, tile.x, abs(x_low), tile.y, abs(y_low), tile.history)
      full_tiles[full_tile.y][full_tile.x] = full_tile

for i, row in enumerate(full_tiles):
  for j, tile in enumerate(row):
    print()
    print(i, j)
    print(tile.y, tile.x)