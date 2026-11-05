''''
pin=1234
for i in range(5):
    epin=int(input("Ennter the the pin:" ))
    if epin == pin:
        print("Login")
        break
    else:
        print("Ivalid pin")
else:
    print("Try again after 30 secs") 
      '''''
'''''
l=[12,34,5,67,89,0]
search=int(input("enter the number: "))
for i in range(len(l)):
    if l[i] == search:
        print(f'{search} is found at index{i}')
        break
else: 
    print(f'{search} is not found')
    '''''
#enumerate
'''''
c='codegnan'
for i in enumerate(c):
    print(i[0],i[1])

c=[1,3,4,5,676,79]
for i in enumerate(c):
    print(i[0],i[1])

c={1,2,3,45,6,77}
for i in enumerate(c):
    print(i[0],i[1])
 '''
'''''
c={'k1':'v1','k2':'v3','k3':'v4'}
for i in enumerate(c):
    print(i[0],i[1],c[i[0]])
    '''''