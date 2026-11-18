#int float str list tuple set dic 
#int float str tuple bool these are imutabple and pass 
#list set dict these are mutable
'''''
def display(n):
    n=False
    print("Inside function:",n)

n=True
display(n)
print("outside function: ",n)
'''
''''
def display(n):
    n+=10
    print("Inside function:",n)

n=10
display(n)
print("outside function: ",n)
'''
''''
def display(n):
    n+=10.3
    print("Inside function:",n)

n=10.3
display(n)
print("outside function: ",n)'''

''''
def display(n):
    n+="programming"
    print("Inside function:",n)

n="python"
display(n)
print("outside function: ",n)'''
''''
def display(n):
    n.append(7)
    print("Inside function:",n)

n=[1,2,3,4]
display(n)
print("outside function: ",n)
'''