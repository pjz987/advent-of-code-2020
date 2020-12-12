from parse_input import parse

evasive_actions = parse('23input.txt')
starting_position = ( 0,  0)
waypoint = (10, -1)

current_pos = starting_position

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
    next_pos_x = waypoint[0] + dir_dict[action][0] * value
    next_pos_y = waypoint[1] + dir_dict[action][1] * value
    waypoint = (next_pos_x, next_pos_y)
  
  elif action in ['L', 'R']:
    if value == 180:
      waypoint = (-waypoint[0], -waypoint[1])

    elif (action == 'L' and value == 90) or (action == 'R' and value == 270):
      waypoint = (waypoint[1], -waypoint[0])

    elif (action =='R' and value == 90) or (action == 'L' and value == 270):
      waypoint = (-waypoint[1], waypoint[0])

    # elif action == 'L':
    #   if value == 90:
    #     # (1, 2) -> (2, -1)
    #     waypoint = (waypoint[1], -waypoint[0])
    #   elif value == 180:
    #     # (1, 2) -> (-1, -2)
    #     waypoint = (-waypoint[0], -waypoint[1])
    #   elif value == 270:
    #     # (1, 2) -> (-2, 1)
    #     waypoint = (-waypoint[1], waypoint[0])
    
    # elif action == 'R':
    #   if value == 90:
    #     # (1, 2) -> (-2, 1)
    #     waypoint = (-waypoint[1], waypoint[0])
    #   if value == 180:
    #     way
  
  elif action == 'F':
    next_pos_x = current_pos[0] + waypoint[0] * value
    next_pos_y = current_pos[1] + waypoint[1] * value
    current_pos = (next_pos_x, next_pos_y)

manhattan_distance = abs(current_pos[0]) + abs(current_pos[1])
print(manhattan_distance)