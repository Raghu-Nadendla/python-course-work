# str list tuple set dict range()

# for in sq:
    #stmt
'''
s='Raghu'
for i in s:
    print(i)
  '''
'''''
a=input("Enter the string:")
for i in a:
    if i in 'aeiouAEIOU':
        print(f'{i} is a vowel')
    else:
        print(f'{i} is a consonant')
        '''
''''
s=['Raghu','Surya','Tulasi','Vivek','Chandra','Mahankali','Rajesh']
for i in s:
    print(i)
   '''''
'''''
l=list(map(int,input("Enter the numbers:").split()))
for i in l:
    if i%2==0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')
 
       '''''
'''''
sumoftuple=0
l=tuple(map(int,input("Enter the numbers:").split()))
for i in l:
    sumoftuple+=i
print(f'sum of tuple is {sumoftuple}')
                        '''''
''''
s={10,20,30,40,50}
max=0
min=10
for i in s:
    if i>max:
        max=i
    elif i<min:
        min=i
print(f'maximum number in set is {max}')
print(f'minimum number in set is {min}')
        '''
'''''
dic={
    'python': 85,
    'java': 90,
    'c++': 80,
    'css': 75
}
for i in dic:
    print(f'{i} is a subject and marks is {dic[i]}')
som=0
for i in dic:
    som+=dic[i]
print(f'sum of dictionary values is {som}')
              '''''
''''
for i in range(1,11):
    print(i)

for i in range(20,0,-1):
    print(i,end=' ')

for i in range(1,101,2):
    print(i,end=' ')
    '''
'''''
n=int(input("Enter the number:"))
for i in range(1,11):
    print(f'{n}*{i}={n*i}')
'''
'''''
s=input("Enter the string:")
for i in range(len(s)):
    print(s[i],i,end=' ')
    '''
''''
s=list(map(int,input("Enter the numbers:").split()))
index=0
sum=0
for i in s:
    if i%2==0:
        index+=1
        sum+=i
print(f'sum of even {sum}count of even numbers {index}')
'''''
'''''
for i in range(1,11):
    if i == 5:
        break
    print(i)

for i in range(1,11):
    if i == 5:
        continue
    print(i)
for i in range(1,10):
    pass
if True:
    pass
class booking:
    pass
def fun():
    pass
    '''