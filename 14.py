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

def bag_count(in_rule, rules, mult_stack=[1]):
  global bag_counter
  mult = mult_stack[-1]
  bag_counter += mult
  print()
  print('count: ', bag_counter)

  inside = in_rule['in']
  if inside == []:
    mult_stack.pop()
  for bag in inside:
    previous_mult = mult
    # print(bag)
    for out_rule in rules:
      if out_rule['out'] == bag['description']:
        # mult *= bag['num']
        mult_stack.append(mult * bag['num'])
        print(bag)
        print(out_rule)
        print(mult_stack)
        bag_count(out_rule, rules, mult_stack)
    

rules_list = parse('13input.txt')
rules = []
for rule in rules_list:
  rule_dict = make_rule_dict(rule)
  rules.append(rule_dict)

bag_counter = 0
for rule in rules:
  if rule['out'] == 'shiny gold':
    bag_count(rule, rules)

print(bag_counter)