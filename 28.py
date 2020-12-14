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
    if bit in ['X', '1']:
      bit_num_masked += bit
    else:
      bit_num_masked += bit_num[i]
  return bit_num_masked

def get_addresses_from_mask(mask, address='', i=0):
  global addresses
  if len(mask) == len(address):
    return addresses.append(address)
  bit = mask[i]
  i += 1
  if bit == 'X':
    address += '1'
    get_addresses_from_mask(mask, address, i)
    address = address[:-1]
    address += '0'
    get_addresses_from_mask(mask, address, i)
  else:
    address += bit
    get_addresses_from_mask(mask, address, i)
    

memory = {}
mask = ''
for line in code:
  if line[0] == 'mask':
    mask = line[1]
    # print('mask:')
    # print(mask)
  else:
    address = int(line[0][4:-1])
    value = int(line[1])
    # print('value: ', value)
    bit_address = to_bits(address)
    # print('address:')
    # print(bit_address)
    bit_address_masked = use_mask(mask, bit_address)
    # print('masked address:')
    # print(bit_address_masked)
    addresses = []
    get_addresses_from_mask(bit_address_masked)
    for bit_address in addresses:
      memory[from_bits(bit_address)] = value
    # num_masked = from_bits(bit_address_masked)
    # memory[mem] = num_masked
    # print(mem)
    # print(num)

print(sum(memory.values()))