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

rules, your_ticket, nearby_tickets = parse_data(data)

errors = []

for ticket in nearby_tickets:
  for num in ticket:
    if check_num(num, rules):
      continue
    else:
      errors.append(num)
      break

print(sum(errors))