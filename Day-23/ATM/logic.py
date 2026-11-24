data = {
    123456:{"pin":1236,"balance":6000,"transanctions":[]},
    123457:{"pin":1237,"balance":6000,"transactions":[]},
    123458:{"pin":1238,"balance":6000,"transactions":[]},
    123459:{"pin":1239,"balance":6000,"transactions":[]}
}

def login():
    global acc_num
    acc_num = int(input("Enter the account number: "))
    epin = int(input("Enter the pin: "))
    if acc_num in data and data[acc_num]['pin'] == epin:
        print("Login successful")
        return True
    else:
        print("Invalid login")
        return False
def menu():
    print()
    print("[C]heck balance")
    print("[D]eposit")
    print("[W]ithdraw")
    print("[T]ransactions")
    print("Change [Pin]")
    print("[E]xit")

def checkbalance():
    print(f"current balance is {data[acc_num]['balance']}")

def deposit():
    amount = int(input("Enter the amount: "))
    data[acc_num]['balance']+=amount
    data[acc_num]['transactions'].append(f"Deposit: {amount}")
    print(f"{amount} deposited successfully")

def withdraw():
    amount = int(input("Enter the amount: "))
    if data[acc_num]['balance'] >= balance:
        data[acc_num]['balance']-=amount
        data[acc_num]["transactions"].append(f"Withdraw: {amount}")
        print(f"{amount} withdrawn successfully")

def transactions():
    if data[acc_num]["transactions"]:
        print("-----------------Transactions-----------------")
        for i in sata[acc-num]['transactions']:
            print(i)
    else:
        print("No transactions yet")

def changepin():
    cpin = int(input("Enter old pin: "))
    if data[acc_num]['pin'] == cpin:
        new_pin = int(input("Enter new pin: "))
        data[acc_num]['pin'] = new_pin
        print("Pin changed successfully")
    else:
        print("Pin does not match")
