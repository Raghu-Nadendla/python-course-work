'''
for row in range(5):
    for col in range(5):
        print('*',end=' ')
    print()
'''
#1 0 1 0 1 
#0 1 0 1 0 
#1 0 1 0 1 
#0 1 0 1 0 
#1 0 1 0 1
''''
for row in range(5):
    for col in range(5):
        print(int((row+col)%2==0),end=' ')
    print()

for row in range(5):
    for col in range(5):
        if (row+col)%2==0:
            print('1',end=' ')
        else:
            print('0',end=' ')
'''
#0 1 0 1 0
#0 1 0 1 0
#0 1 0 1 0
#0 1 0 1 0
#0 1 0 1 0
''''
for row in range(5):
    for col in range(5):
        if (col)%2:
            print('1',end=' ')
        else:
            print('0',end=' ')
    print()

for row in range(5):
    for col in range(5):
        print(int(col)%2),end=' ')
    print()
'''''
''''
count=1
for row in range(5):
    for col in range(5):
            print(count,end=' ')
            count+=1
    print()
'''''
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
'''''
for row in range(5):
    for col in range(5):
         print(row*col,end='')
    print()
'''''
#*
#* *
#* * *
#* * * *
#* * * * *
'''''
for row in range(5):
    for col in range(row+1):
        print("*",end=' ')
    print()
'''''
#* * * * * 
#* * * * 
#* * * 
#* * 
#* 
'''''
for row in range(5):
    for col in range(row,5):
        print("*",end=' ')
    print()
'''
