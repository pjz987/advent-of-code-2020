# not mine wzkx from the subreddit... trying to understand it

d = open("25input.txt","rt").read().splitlines()

t = int(d[0])
b = {i:int(x) for i,x in enumerate(d[1].split(",")) if x!='x'}

print(b)
print(type(b))

s = min((n-t%n,n) for n in b.values())
print(s[0]*s[1])

def step(s,n,n2,k2):
  f = (n2-k2)%n2
  for r in range(s,9999999999999999,n):
    if r%n2==f:
      return r
  raise "no answer"

a = sorted((v,i) for i,v in b.items())
n = 1
r = a[-1][0]-a[-1][1]
for i in range(1,len(a)):
  n *= a[-i][0]; n2,k2 = a[-i-1]
  r = step(r,n,n2,k2)
print(r)