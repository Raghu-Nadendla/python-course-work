''''
for row in range(5):
    for space in range(5-row):
        print(" ",end=' ')
    for col in range(row+1):
        print("*",end=' ')
    print()
'''
#* * * * * 
#   * * * * 
#      * * * 
#        * * 
#           * 
'''''
for row in range(5):
    for space in range(row):
        print(" ",end=' ')
    for col in range(5-row):
        print("*",end=' ')
    print()
'''''
#hill pattern
''''
n=int(input())
m=n//2
for row in range(n):
    if row<=m:
        for col in range(row+1):
            print("*",end=' ')
    else:
        for col in range(n-row):
            print("*",end=' ')
        
    print()
'''
'''''
n=int(input())
m=n//2
for row in range(n):
    if row<=m:
        print('*'*(row+1))
    else:
        print('*'*(n-row))
'''''

'''''
n=int(input())
m=n//2
for row in range(n):
    print('*'*(row+1) if row<=m else '*'*(n-row) )
    '''
'''''
n=int(input())
m=n//2
for row in range(n):
    for col in range(n):
        if row == 0 or col == 0 or row == n-1 or col == n-1 or row == m or col == m:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''''
'''''
n=int(input())
m=n//2
for row in range(n):
    for col in range(n):
        if row == 0 or col == 0 or row == n-1 or col == n-1 or row == m or col == m  or row+col == n-1:
                print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''
# G alaphabet
'''''
n=int(input())
m=n//2
for row in range(n):
    for col in range(n):
        if row == 0 or col == 0 or row == n-1 (col == n-1 and row>=m) or (row==m and col>=m):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
    '''
#j alaphabet
'''''
n=int(input())
m=n//2
for row in range(n):
    for col in range(n):
        if row == 0 or col == m or(row == n-1 and col<=m) or (col==0 and row >=m):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#M alaphabet

n=int(input())
m=n//2
for row in range(n):
    for col in range(n):
        if col == 0 or col == n-1 or (row==col and row<=m) or (row+col == n-1 and row <=m):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()