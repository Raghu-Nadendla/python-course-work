#var lambda =args:sts
# lambda function work on if esle & nested if 

'''
sol=lambda a,b,c: a+b+c
print(sol(10,20,30))


gst =lambda price:price+price*0.18
print(gst(1000))


avg =lambda l:sum(l)/len(l)
l=[99,34,65,78,66]
print(avg(l))


iseven =lambda n:"Even" if n%2==0 else "Odd"
print(iseven(10))
print(iseven(17))


isvowel = lambda ch :"Vowel" if ch in 'aeiouAEIOU' else "Consonant"
print(isvowel('a'))
print(isvowel('z'))'''

#nested if 
''''
check=lambda data,pro: (f"product price:{data[pro]['price']}" if data[pro]["stock"]>0 else "out of stock") if pro in data else "product is unavaliable"
data={
    'apple':{'stock':10,'price':50},
    'banana':{'stock':10,'price':50},
    'guva':{'stock':89,'price':100},
    'sapota':{'stock':0,'price':300},
    'cocount':{'stock':49,'price':500},

}

print(check(data,'sapota'))'''
'''
def add(l):
    for i in range(len(l)):
        l[i]+=10
    return l

l=[6,7,8,9,3,33,3]
print(add(l))'''
''''
def domain(d):
    for i in range(len(d)):
        d[i]=(d[i].split('@')[1]).split('.')[0]
    return d
d=["raghu@gmail.com","raghu@yahho.com","rtyui@gmail.com"]
print(domain(d))'''

''''
def cu(c):
    for i in range(len(c)):
        c[i] = c[i].upper()
    return c

c = ["raghu", "raghava"]
print(cu(c))'''
# lambda function with map is update 

''''
l=[9,3,4,4,5,55]
addten=list(map(lambda i:i+10,l))
print(addten)

d=['xyz@codegnan.com','abc@gmail.com','pqrs@yahoo.com']
domain=list(map(lambda i:(i.split('@')[1]).split('.')[0],d))
print(domain)


c=['raghu','raghava','wertyuio']
cu=list(map(lambda i:i.upper(),c))
print(cu)

d={'a':20,'b':40,'c':50}
gst=dict(map(lambda i:(i[0],i[1],+i[1]*0.18),d.items()))
print(gst)'''

# lambda using filter use baed on condition
''''
l=[1,2,3,4,5,56,7,7,7.88,8]
even=list(filter(lambda i:i%2==0,l))
print(even)

a=['a','e','i','d','o','u']
vowels=list(filter(lambda i: i in 'aeiouAEIOU',a))
print(vowels)'''

# reduce 
'''
from functools import reduce

l=[2,3,4,5,6,7,8,89]
sumofl = reduce(lambda sum,i:sum+i,l)

print(sumofl)'''