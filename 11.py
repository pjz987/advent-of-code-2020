from parse_input import parse3
from string import ascii_lowercase

group_answers = parse3('11input.txt')
yes_answers = 0
for group in group_answers:
  for letter in ascii_lowercase:
    if letter in group:
      yes_answers += 1
print(yes_answers)