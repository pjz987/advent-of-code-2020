from parse_input import parse
import re

expressions = parse('35input.txt')

parens_match = r'\(([0-9]|\*|\+|\s)*\)'

test = '2 * 3 + (4 * 5)'
test = '1 + (2 * 3) + (4 * (5 + 6))'

def linear_math(expression):
  expression = expression.split()
  num = 0
  operator = ''
  operators = ['*', '+']
  for i, char in enumerate(expression):
    if i == 0:
      num = char
    elif char in operators:
      operator = char
    else:
      num = eval(str(num) + operator + char)
  return num

def evaluate(expression):
  match = re.search(parens_match, expression)
  if match:
    sub_expression = match.group().strip('()')
    sub_range = match.span()
    pre_expression = expression[0:sub_range[0]]
    post_expression = expression[sub_range[1]:]
    return evaluate(pre_expression + str(linear_math(sub_expression)) + post_expression)
  return linear_math(expression)

print(evaluate(test))

evaluated_expressions = [evaluate(expression) for expression in expressions]
print(sum(evaluated_expressions))