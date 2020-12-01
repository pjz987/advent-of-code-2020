from parse_input import parse

def get_2020_mult(input_list):
  for number1 in input_list:
    for number2 in input_list:
      if number1 + number2 == 2020:
        return number1 * number2

print(get_2020_mult(parse('01input.txt')))
