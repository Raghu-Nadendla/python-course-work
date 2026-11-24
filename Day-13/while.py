#int
#while cond:
#stmt
#upd
'''
l=[1,0,0,0,0,0,3,0,0,3,0,4,0,4,0,0,5,9,9,5,]
while 0 in l:
    l.remove(0)
print(l)
'''
'''''
i=1
while i<11:
    print(i)
    i+=1

i=2
while i<100:
    print(i)
    i+=2

i=5
while i<100:
    print(i)
    i+=5
    '''
'''#string
a="raghu"
i=0
while i<len(a):
    print(i,a[i])
    i+=1
    '''
'''
a=[1,2,3,4,5,6]
i=0
while i<len(a):
    print(i,a[i])
    i+=1

a=(2,5,67,8,9)
i=0
while i<len(a):
    print(i,a[i])
    i+=1
    '''
''''
a=[1,2,3,4,5]
i=0
while i<len(a):
    if a[i]==5:
        break
    print(i,a[i])
    i+=1

a=[1,2,3,4,5]
i=0
while i<len(a)-1:
    i+=1
    if a[i]==5:
        continue
    print(i,a[i])
    '''
''''
c=input("enter the name:")
i=0
j=len(c)-1
while i<=j:
    if i==j:
        print(c[i])
    else:
        print(c[i],c[j])
    i+=1
    j-=1
    '''