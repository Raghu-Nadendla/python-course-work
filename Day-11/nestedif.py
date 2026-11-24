'''
login=True
payment=True
product_available=True
if login:
    print("login successful")
    if product_available:
        print("product is available")
    else:
        print("product is not available")
        if payment:
            print("payment successful")
        else:
            print("payment failed")
else:
    print("login failed")
'''
''''
data={
    'raghu':{'status':True,'python':95,'java':93,'css':92},
    'surya':{'status':True,'python':84,'java':83,'css':81},
    'tulasi':{'status':True,'python':75,'java':74,'css':73},
    'vivek':{'status':True,'python':50,'java':52,'css':60},
    'chandra':{'status':True,'python':60,'java':67,'css':69},
    'mahankali':{'status':True,'python':56,'java':55,'css':68},
    'rajesh':{'status':False,'python':None,'java':None,'css':None}
    }
name =input("Enter the name: ")
if name in data:
    print(f'{name} is a student')
    if data[name]['status']: 
        total=data[name]['python']+data[name]['java']+data[name]['css']
        average=total/3
        if average>=90:
            print(f'{name} is a topper with average marks of {average}')
        elif average>=80:
            print(f'{name} is a good student with average marks of {average}')
        elif average>=70:
            print(f'{name} is a average student with average marks of {average}')
        elif average>=60:
            print(f'{name} is a below average student with average marks of {average}')
        elif average>=50:
            print(f'{name} is a poor student with average marks of {average}')
        else:
            print(f'{name} is a failed student with average marks of {average}')
    else:
        print(f'{name} bring paents to school for inactive status')
else:
    print(f'{name} is not a student')
    '''
