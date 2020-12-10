from parse_input import parse_sort

adapters = parse_sort('19input.txt')
adapters.append(0)
adapters.sort()
jolt_differences = {
  1: 0,
  2: 0,
  3: 0
}

for i, adapter in enumerate(adapters):
  if i == len(adapters) - 1:
    jolt_differences[3] += 1
    break
  next_adapter = adapters[i + 1]
  jolt_difference = next_adapter - adapter
  jolt_differences[jolt_difference] += 1

print(jolt_differences[1] * jolt_differences[3])