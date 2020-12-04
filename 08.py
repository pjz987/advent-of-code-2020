from parse_input import parse2
import string

batch = parse2('07input.txt')

for i, passport in enumerate(batch):
  keys = []
  values = []
  for field in passport:
    keys.append(field.split(':')[0])
    values.append(field.split(':')[1])
  batch[i] = dict(zip(keys, values))

valid_passports = 0

required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
required_fields_cid = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}

batch_stage_2 = []
for passport in batch:
  if set(passport.keys()) == required_fields or set(passport.keys()) == required_fields_cid:
    batch_stage_2.append(passport)
  
for passport in batch_stage_2:
  if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
    continue
  if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
    continue
  if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
    continue
  if passport['hgt'][-2:] not in ['cm', 'in']:
    continue

  if passport['hgt'][-2:] == 'cm':
    if len(passport['hgt']) != 5:
      continue
    if int(passport['hgt'][:3]) < 150 or int(passport['hgt'][:3]) > 193:
      continue

  if passport['hgt'][-2:] == 'in':
    if len(passport['hgt']) != 4:
      continue
    if int(passport['hgt'][:2]) < 59 or int(passport['hgt'][:2]) > 76:
      continue

  if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
    continue
  if passport['hcl'][0] != '#' or len(passport['hcl']) != 7:
    continue

  hcl = True
  for char in passport['hcl'][1:]:
    if char not in string.hexdigits:
      hcl = False
  
  if len(passport['pid']) != 9:
    continue

  pid = True
  for digit in passport['pid']:
    if digit not in string.digits:
      pid = False
  
  if hcl and pid:
    valid_passports += 1

print(valid_passports)

  