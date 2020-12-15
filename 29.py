import sys
sys.setrecursionlimit(5000)

numbers = [5, 2, 8, 16, 18, 0, 1]
# numbers = [0, 3, 6]

def play_game():
  global numbers
  last_num = numbers[-1]
  if len(numbers) == 2020:
    return last_num

  if last_num in numbers[:-1]:
    i = len(numbers) - 1
    while True:
      i -= 1
      if numbers[i] == last_num:
        numbers.append(len(numbers) - 1 - i)
        break
    return play_game()

  else:
    numbers.append(0)
    return play_game()

print(play_game())