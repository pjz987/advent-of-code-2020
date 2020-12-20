from parse_input import parse_string
recursions = 0

def check_rule(rule):
  global test_message
  global rule_stack
  global rules

  for i, value in enumerate(rule):
    for j, key in enumerate(value):
      rule_stack.append(key)
      char = validate_message(message)
      test_message += char

      if test_message != message[:len(test_message)]:
        rule_stack.pop()
        return


def validate_message(message: str):
  global test_message
  global rule_stack
  global rules

  if message == test_message:
    return True

  rule_key = rule_stack[-1]
  rule = rules[rule_key]

  if rule in ['a', 'b']:
    rule_stack.pop()
    return rule

  else:
    broken = False
    for j, value in enumerate(rule):
      for i, key in enumerate(value):
        rule_stack.append(key)
        char = validate_message(message, test_message)
        test_message += char

        if test_message != message[:len(test_message)]:
          test_message = test_message[:-1 - abs(i)]
          broken = True
          break
        elif i == len(value) - 1:
          for _ in range(i + 1):
            rule_stack.pop()
          return validate_message(message, test_message)
        

      if broken:
        if j == len(rule) - 1:
          rule_stack.pop()
        continue
      return validate_message(message, test_message)
        


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

matches = 0
for message in messages[:1]:
  test_message = ''
  message_validated = validate_message(message)
  print(message_validated)
  if message_validated:
    matches += 1
print(matches)