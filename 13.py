from parse_input import parse

def make_rule_dict(rule):
  rule_dict = {}
  out = rule.split(' bags contain ')[0]
  inside = rule.split(' bags contain ')[1].strip('.').split(', ')
  rule_dict['out'] = out
  rule_dict['in'] = make_inside_dict_list(inside)
  return rule_dict

def make_inside_dict_list(inside_in):
  if inside_in == ['no other bags']:
    return []
  inside_out = []
  for bag in inside_in:
    num_description = {}
    num_description['num'] = int(bag.split(' ')[0])
    num_description['description'] = bag.split(' ')[1] + ' ' + bag.split(' ')[2]
    inside_out.append(num_description)
  return inside_out

def bag_search(in_rule, rules, search_bag='shiny gold'):
  inside = in_rule['in']
  if inside == []:
    print(in_rule)
  for bag in inside:

    description = bag['description']
    if description == search_bag:
      print(rule)
      return True

    for out_rule in rules:
      if out_rule['out'] == description:
        next_rule = out_rule
        print(description)
        print(out_rule)
        if next_rule['in'] != []:
          if bag_search(next_rule, rules):
            return True
    

rules_list = parse('13input.txt')
rules = []
for rule in rules_list:
  rule_dict = make_rule_dict(rule)
  rules.append(rule_dict)

bag_color_count = 0
for rule in rules:
  # print(rule)
  # for bag in rule['in']:
    # if bag['description'] == 'shiny gold':
    #   print(rule)
  if bag_search(rule, rules):
    bag_color_count += 1
  print('*'*100)

print(bag_color_count)