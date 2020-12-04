from parse_input import parse2

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

for passport in batch:
  if set(passport.keys()) == required_fields or set(passport.keys()) == required_fields_cid:
    valid_passports += 1
print(valid_passports)