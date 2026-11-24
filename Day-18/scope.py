#local scope A local variable is created ""inside a function""". You can use it inside that function.
#gobal scope A global variable is created ""outside a function""". You can use it in different parts of the program.
#gobal non local     nonlocal means inside an outer function.
#build scope 
'''''
def display():
    global n
    n=10
    print("inside:",n)

display()
print("outside:",n)'''

#local scope
''''
def show_message():
    message = "Hello"  # local variable
    print(message)

show_message()  # Hello
print(show_message)  # Error: message is not available here '''

#gobal scope
''''
name = "Raghu"  # global variable

def greet():
    print("Hello", name)

greet()  # Hello Raghu
print(name)  # Raghu'''

#gobal non local 
''''
def display():
    course="jfs"
    print("Starting: ",course)
    def update():
        nonlocal course
        course="pfs"
        print("update: ",course)
    update()
    print("update: ",course)


display()
'''

# build scope You can use them without creating them yourself or importing a module.
''''
numbers = [4, 7, 2]

print(len(numbers))  # 3
print(max(numbers))  # 7
'''