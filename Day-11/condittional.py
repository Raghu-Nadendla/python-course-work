# if -else
'''
data =('admin@gmail.com','admin@122')

gmail=("Enter the gmail:")
password=("Enter the password:")

if(gmail,password)==data:
    print("login successful")
else:
    print("login failed")
    '''
'''
seats={
    's1':'Booked',
    's2':'Available',
    's3':'Booked',
    's4':'Available',
    's5':'Available',
    's6':'Booked'
}

seatno=input("Enter the seat number: ")
if seatno in seats and seats[seatno]=='Available':
    seats[seatno]='Booked'
    print(f'{seatno} is available for booking')
    print(seats)

else:
    print(f'{seatno} is not available for booking')
'''
'''
blance=5000
payment=int(input("Enter the payment amount: "))

if payment<=blance:
    print('payment successful')
    
else:
    print('payment failed')
   ''' 

products={
    'p1':{'name':'laptop','price':50000,'stock':5},
    'p2':{'name':'mobile','price':20000,'stock':10},
    'p3':{'name':'headphones','price':2000,'stock':15},
    'p4':{'name':'keyboard','price':1000,'stock':20},
    'p5':{'name':'mouse','price':500,'stock':25}
}
'''
search_product=(input("Enter the product number to search: "))
if search_product in products:
    print(f'you can buy{search_product} for {products[search_product]["name"]})')
else:
    print(f'{search_product} is not available in the store')
    '''

