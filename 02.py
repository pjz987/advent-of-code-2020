from parse_input import parse

def get_2020_triple_mult(input_list):
  for number1 in input_list:
    for number2 in input_list:
      for number3 in input_list:
        if number1 + number2 + number3 == 2020:
          return number1 * number2 * number3

print(get_2020_triple_mult(parse('01input.txt')))
  