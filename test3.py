from random import randint
import time

start = time.time()
nums = []
for _ in range(30000000):
    nums.append(randint(0, 30000000))

loop = time.time()
num = randint(0, 30000000)
print(num in set(nums))
end = time.time()

print(loop - start)
print(end - loop)
