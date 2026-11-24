#sys module
''''
import sys

print(sys.argv)
print(sys.path)
print(sys.version)
sys.exit()
print("hello world")'''


# platfrom module
'''
import platform

print(platform.system(),platform.release(),platform.processor(),sep='\n')'''

#math module
'''
import math

print(math.pi)
print(math.e)

print(math.sqrt(16))

print(math.pow(3,3))
print(math.pow(2,3))

print(round(12.55555))
print(round(12.8))
print(round(13.2))

print(math.ceil(12.3))
print(math.ceil(13.1))
print(math.ceil(12.000))

print(math.factorial(6))

print(math.gcd(12,16))
print(math.log(2.2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(128))
print(math.radians(120))'''

#random module
''''
import random 

print(random.random())
print(random.randint(1,10))
print(random.uniform(1,10))

l=['python','java','css','html','flask']

print(random.choice(l))
print(random.choices(l,k=3))

print(l)
random.shuffle(l)
print(l)

random.seed(10)'''

#collections
'''
from collections import Counter,deque

s="python programming"

print(Counter(s))

d={}

for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)

from collections import Counter,defaultdict

s="python programming"

d=defaultdict(float)

for i in s:
    d[i]+=1
print(d)

s=deque([])
s.append(10)
s.append(20)
s.append(30)
s.append(40)
s.popleft()
s.popleft()
s.popleft()

print(s)

s=deque([])
s.appendleft(10)
s.appendleft(20)
s.appendleft(30)
s.appendleft(40)
s.pop()
s.pop()

print(s)
'''

# itertools
''''
from itertools import combinations,permutations

s='abcd'


print([''.join(i) for i in combinations(s,3)])
print([''.join(i)for i in permutations(s,3)])
'''