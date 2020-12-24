from parse_input import parse
import numpy
import re

directions = parse('47input.txt')
# for direction in directions:
#     print(direction)

all_dirs = r'(n|ne|e|se|s|sw|w|nw)*'
one_dir = r'(n|ne|e|se|s|sw|w|nw){1}'

test = 'sesenwnenenewseeswwswswwnenewsewsw'

test_list = re.findall(one_dir, test)
print(test_list)
print(test)
print(''.join(test_list))