import logic as lg

if lg.login():
    print("Welcome to SmartATM")
    while True:
        lg.menu()
        ch=input("Enter the choice: ").upper()
        if ch=='C':
            lg.checkbalance()
        elif ch=='D':
            lg.deposit()
        elif ch=='W':
            lg.withdraw()
        elif ch=='T':
            lg.transactions()
        elif ch=='P':
            lg.changepin()
        elif ch=='E':
            print("Thank you visit again")
            break
        else:
            print("Invalid input,try again")
