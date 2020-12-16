from parse_input import parse_newlines

data = parse_newlines('31input.txt')

def parse_data(data):
  rules = data[0].split('\n')
  rules = parse_rules(rules)
  your_ticket = data[1].split('\n')
  your_ticket = parse_your_ticket(your_ticket)
  nearby_tickets = data[2].split('\n')
  nearby_tickets = parse_nearby_tickets(nearby_tickets)
  return rules, your_ticket, nearby_tickets

def parse_rules(rules):
  rules_dict = {}
  for rule in rules:
    key, values = rule.split(':')
    values = values.strip().split(' or ')
    values = [value.split('-') for value in values]
    rules_dict[key] = [range(int(value[0]), int(value[1]) + 1) for value in values]
  return rules_dict

def parse_your_ticket(your_ticket):
  return [int(num) for num in your_ticket[1].split(',')]

def parse_nearby_tickets(nearby_tickets):
  return [[int(num) for num in ticket.split(',')] for ticket in nearby_tickets[1:]]

def check_num(num, rules):
  for ranges in rules.values():
    if num in ranges[0] or num in ranges[1]:
      return True

def discard_invalid_tickets(nearby_tickets, errors):
  for i, ticket in enumerate(nearby_tickets):
    for num in ticket:
      if num in errors:
        nearby_tickets.pop(i)
        return discard_invalid_tickets(nearby_tickets, errors)

def find_matches(ticket, rules, no_false_dict):
  matches_list = []
  for i, num in enumerate(ticket):
    num_dict = {}
    num_dict['num'] = num
    for rule in rules.keys():
      values = rules[rule]
      if num in values[0] or num in values[1]:
        num_dict[rule] = True
      else:
        num_dict[rule] = False
        no_false_dict[i].remove(rule)
    matches_list.append(num_dict)
  return matches_list
      
rules, your_ticket, nearby_tickets = parse_data(data)

errors = []

for ticket in nearby_tickets:
  for num in ticket:
    if check_num(num, rules):
      continue
    else:
      errors.append(num)
      break

discard_invalid_tickets(nearby_tickets, errors)

def get_true_rules(no_false_dict, true_rules={}, i=0):
  i += 1
  for key, values in no_false_dict.items():
    if len(values) == i:
      for value in values:
        if value not in true_rules.values():
          true_rules[key] = value
  if i == len(no_false_dict.keys()):
    return true_rules
  return get_true_rules(no_false_dict, true_rules, i)


no_false_dict = {}
for i in range(len(nearby_tickets[0])):
  no_false_dict[i] = [rule for rule in rules.keys()]


for i, ticket in enumerate(nearby_tickets):
  ticket = find_matches(ticket, rules, no_false_dict)
  nearby_tickets[i] = ticket

true_rules = get_true_rules(no_false_dict)

departures = []
for i, num in enumerate(your_ticket):
  if 'departure' in true_rules[i]:
    departures.append(num)
  
product = 1
for num in departures:
  product *= num

print(product)