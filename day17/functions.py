#Basic syntax
'''''
def function_name():
    statements
function_name()
'''
# prime Number using Function
''''
def factors(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c>2:
        print("Not prime number")
    else:
        print("prime number")

factors(int(input("Enter the number")))
'''
'''''
def isprime(n):
    for i in range(1,n+1):
        if n%i==0:
            return "Not prime Number"  #return function used to send a result from a function back to the place where the function was called.
    return "prime number"

print(isprime(int(input("Enter the number"))))

'''
# sum of digits
''''
def sum(n):
    total=0
    for i in range(1,n+1):
        total+=1
    return total
n = int(input("Enter a number: "))

result = addition(n)

print("Sum of numbers:", result)
'''''
''''
def sum(n):
    sum=0
    while n>0:
        sum+=n%10
        n//=10
    return sum

print(sum(34567))
'''

# reverse the numbers
''''
def revs(n):
    sum=0
    while n>0:
        sum=(sum*10)+n%10
        n//=10
    return sum
print(revs(1234))
'''

# positional arguments
#Positional arguments are values passed to a function based on their position or order
'''''
def display(name,email,password):
    print("name:",name)
    print("email:",email)
    print("passwor:",password)

display("abc","abc@gmail.com","abc@123")
'''
# key word arguments
#Keyword arguments are arguments passed to a function by specifying the parameter names along with their values
''''
def display(name,email,password):
    print("name:",name)
    print("email:",email)
    print("passwor:",password)

display(name="abc",email="abc@gmail.com",password="abc@123")
display(password="abc@123",email="abc@email.com",name="abc")
'''
# default arguments
# Default arguments are values assigned to function parameters during function definition. If the user does not provide a value while calling the function, Python automatically uses the default value
'''''
def display(name,email,password,phonenumber=None):
    print("name:",name)
    print("email:",email)
    print("passwor:",password)
    print("phonenumber:",phonenumber)

display("abc","abc@gmail.com","abc@123")
display("abrtyu","dfghjk@gmail.com","ertyu@123",1234567890)
'''
# Variable-length arguments: *args
''''
def display(*n):
    print(n)

display(1,2,3,4)
display(1,2,3)
display(1,2)
'''

''''
def student():
    marks = {
        "Raghu": 95,
        "Surya": 80,
        "Ravi": 65
    }

    highest = max(marks, key=marks.get)
    lowest = min(marks, key=marks.get)

    print("Student Details:", marks)
    print("Highest Marks:", highest, marks[highest])
    print("Lowest Marks:", lowest, marks[lowest])

student()
'''
