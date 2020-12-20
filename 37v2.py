from parse_input import parse_string
import sys
sys.setrecursionlimit(20000)

class Rule:
  global rules
  def __init__(self, key, value):
    self.key = key
    self.character = value if value in ['a', 'b'] else None
    self.values = None if self.character else value
  
  def find_all(self, message=''):
    if self.character:
      return message + self.character
    for value in self.values:
      for key in value:
        message += self.find_all(message)
    all_valid.append(message)

  def check(self, message, test_message=''):
    if message == test_message:
      return True
    for value in self.values:
      for key in value:
        next_rule = rule_object_dict[key]
        if next_rule.character:
          if test_message + next_rule.character == message[:len(test_message) + 1]:
            test_message += next_rule.character
          else:
            break
        else:
          return next_rule.check(message, test_message)
    # return test_message
        
  def __repr__(self):
    return f"""
      key: {str(self.key)}
      character: {str(self.character)}
      values: {str(self.values)}
    """

raw = parse_string('37input_test.txt')
rules_raw = raw.split('\n\n')[0].strip()
messages_raw = raw.split('\n\n')[1].strip()
rule_stack = [0]

rules = {}
for rule in rules_raw.split('\n'):
  key = int(rule.split(':')[0])
  values = []
  values_raw = rule.split(':')[1].strip()
  if values_raw in ['"a"', '"b"']:
    rules[key] = values_raw.strip('"')
  else:
    for value in values_raw.split(' | '):
      values.append(tuple([int(num) for num in value.split()]))
    rules[key] = tuple(values)




messages = messages_raw.split()

rule_objects = [Rule(key, value) for key, value in rules.items()]
rule_object_dict = {}
for rule_object in rule_objects:
  rule_object_dict[rule_object.key] = rule_object


rule = rule_objects[0]

all_valid = []
rule.find_all()
print(all_valid)
