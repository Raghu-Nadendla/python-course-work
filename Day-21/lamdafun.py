''''
s={'s1':True,'s2':True,'s3':False,'s4':True,'s5':True}
d={'a':900,'b':200,'c':1000,'d':505}

bokked=dict(filter(lambda i:i[1]==True,s.items()))
unbokked=dict(filter(lambda i:i[1]!=True,s.items()))

gst=dict(map(lambda i:(i[0],i[1]+i[1]*0.18),d.items()))
gre=dict(filter(lambda i:i[1]>500,d.items())) 


print(bokked)
print(unbokked)

print(gst)
print(gre)'''
''''
d={'laptop':9000,'camera':10000,'mobile':5000}

print(dict(sorted(d.items())))
print(dict(sorted(d.items(),reverse=True)))

print(dict(sorted(d.items(),key=lambda i:i[1])))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))'''

#Generator : A generator is a special type of function in Python that uses the yield keyword to return values one at a time instead of returning all values at once.
#Memory Efficient: Generators save memory because they produce values only when needed, rather than storing all values in memory.

''''
def reels():
    res=('1-100','101-200','201-300','301-400','401-500','501-600','600-7')
    yield res[0]
    yield res[1]
    yield res[2]
    yield res[3]
    yield res[4]
    yield res[5]
    yield res[6]

feed =reels()
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))

def reels():
    res=('1-100','101-200','201-300','301-400','401-500','501-600','600-7')
    for i in res:
        yield i

feed =reels()
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))

def reels():
    res=('1-100','101-200','201-300','301-400','401-500','501-600','600-7')
    for i in res:
        yield i
feed = reels()
for i in feed:
    print(i)'''
''''
def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i
n=int(input("Enter the number:"))

for i in factors(n):
    print(i, end=" ")'''
'''''
def prime(n):
    for i in range(2,n+1):
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            yield i
res =prime(50)
for i in res:
    print(i)'''
''''
def fib(n):
    if n==1:
        yield 0
    elif n>=2:
        a,b=0,1
        yield a
        yield b
        for _ in range(n-2):
            c=a+b
            a=b
            b=c
            yield c
res =fib(4)
for i in res:
    print(i)'''


''''
n = int(input("Enter number: "))

for i in range(n):
    for j in range(n):
        if j == 0 or j == n - 1 or i == j:
            print("*", end="")
        else:
            print(" ", end="")
    print()'''