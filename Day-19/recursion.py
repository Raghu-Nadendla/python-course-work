# 1 to 10
''''
def display(n):
    if n>10:
        return
    print(n)
    display(n+1)
display(1)'''

# factoral number using recursuion
'''''
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(6))'''
#10 t0 1
''''
def display(n):
    if n<1:
        return
    print(n)
    display(n-1)
display(10)'''
'''
def dispaly(n):
    if n>10:
        return 
    dispaly(n+1)
    print(n)
dispaly(1)'''

# s ="python programming" -> p y t h o n  p r o g r a m m i n g
''''
def display(n):
    if n == len(s):
        return 
    print(s[n])
    display(n+1)
s="python programming"
display(0) '''
# reverse the string
'''
def dispaly(n):
    if n == len(s):
        return
    print(s[n],end=' ')
    display(n+1)
    print(s[n],end=' ')

s="python programming"
display(0)'''
'''
def display(n):
    for row in range(n):
        for col in range(row+1):
            print("*",end=' ')
        else:
            print(" ",end=' ')
        print()
display(4)'''
#slicing 
'''
def display(n):
    if n == len(s):
        return
    print(s[:n+1])
    display(n+1)
s="python"
display(0)'''
#codegnan -> cod ode deg gna nan
''''
def display(n,c):
    if n>len(s)-c:
        return
    print(s[n:n+c])
    display(n+1,c)
s="codegnan"
display(0,3)'''
#sum of numbers
'''''
def sum(n):
    if n<1:
        return 0
    return n+sum(n-1)
print(sum(10))'''
'''''
def sum(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total
print(sum(11))'''

