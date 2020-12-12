from parse_input import parse

evasive_actions = parse('23input.txt')
starting_position = (0, 0)

current_position = starting_position
facing = 'E'
turn_dict = {
  'E': {
    'L': {
      90 : 'N',
      180: 'W',
      270: 'S'
    },
    'R': {
      90 : 'S',
      180: 'W',
      270: 'N'
    }
  },

  'S': {
    'L': {
      90 : 'E',
      180: 'N',
      270: 'W'
    },
    'R': {
      90 : 'W',
      180: 'N',
      270: 'E'
    }
  },

  'W': {
    'L': {
      90 : 'S',
      180: 'E',
      270: 'N'
    },
    'R': {
      90 : 'N',
      180: 'E',
      270: 'S'
    }
  },

 'N': {
    'L': {
      90 : 'W',
      180: 'S',
      270: 'E'
    },
    'R': {
      90 : 'E',
      180: 'S',
      270: 'W'
    }
  }
}

dir_dict = {
  'N': ( 0, -1),
  'S': ( 0,  1),
  'E': ( 1,  0),
  'W': (-1,  0)
}

for evasive_action in evasive_actions:
  action = evasive_action[0]
  value = int(evasive_action[1:])

  if action in ['N', 'S', 'E', 'W']:
    next_position_x = current_position[0] + dir_dict[action][0] * value
    next_position_y = current_position[1] + dir_dict[action][1] * value
    current_position = (next_position_x, next_position_y)
  
  elif action in ['L', 'R']:
    facing = turn_dict[facing][action][value]
  
  elif action == 'F':
    next_position_x = current_position[0] + dir_dict[facing][0] * value
    next_position_y = current_position[1] + dir_dict[facing][1] * value
    current_position = (next_position_x, next_position_y)

manhattan_distance = abs(current_position[0]) + abs(current_position[1])
print(manhattan_distance)