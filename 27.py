from parse_input import parse

raw_code = parse('27input.txt')

code = [line.split(' = ') for line in raw_code]
bits = [1]
for i in range(1, 36):
  bits.append(bits[i - 1] * 2)
bits.reverse()

def to_bits(integer):
  bit_num = ''
  for bit in bits:
    if integer >= bit:
      integer -= bit
      bit_num += '1'
    else:
      bit_num += '0'
  return bit_num

def from_bits(bit_num):
  integer = 0
  for i, bit in enumerate(bit_num):
    if bit == '1':
      integer += bits[i]
  return integer

def use_mask(mask, bit_num):
  bit_num_masked = ''
  for i, bit in enumerate(mask):
    if bit != 'X':
      bit_num_masked += bit
    else:
      bit_num_masked += bit_num[i]
  return bit_num_masked

memory = {}
mask = ''
for line in code:
  if line[0] == 'mask':
    mask = line[1]
    # print(mask)
  else:
    mem = int(line[0][4:-1])
    num = int(line[1])
    bit_num = to_bits(num)
    bit_num_masked = use_mask(mask, bit_num)
    num_masked = from_bits(bit_num_masked)
    memory[mem] = num_masked
    # print(mem)
    # print(num)

print(sum(memory.values()))