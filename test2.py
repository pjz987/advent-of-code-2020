import time

start = time.time()
count = 0
for _ in range(30000000):
    count += 1

print(count)
end = time.time()
print(end - start)
print(30*(end - start))
