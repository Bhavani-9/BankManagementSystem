from datetime import datetime

customer_names=["Hiral","Bhavani","Ambika"]
customer_pins=["1234","5678","9876"]
customer_amount=[10000,20000,30000]

def NewAccount():
    print("Selected option number",option)
    noc=int(input("Enter number of customers:"))
    i=0
    counter_1=1
    counter_2=3
    i=i+noc
    if i>4:
        print("Customers you have entered are more")
        i=i-noc
    else:
        while counter_1<=i:
            cus_name=input("Enter your name:")
            customer_names.append(cus_name)
            cus_pin=input("Enter the pin")
            customer_pins.append(cus_pin)
            deposit_amt=int(input("Enter your deposit amount:"))
            customer_amount.append(deposit_amt)
            print("\nName :",end="")
            print(customer_names[counter_2])
            print("Pin :", end="")
            print(customer_pins[counter_2])
            print("Balance :",end="")
            print(customer_amount[counter_2],end="")
            print("/-Rs")
            counter_1=counter_1+1
            counter_2=counter_2+1
            print("\nYour details are added into our customer's list")
            print("---Your account is created successfully---")
            print("\nThank you for choosing Moon Bank")
            print("\nPlease remember your account name and pin")
            print("="*25)

def deposit_fun():
    balance=0
    j=0
    print("Selected option number",option)
    while j < 1:
        k = -1
        name=input("Enter your name to deposit:")
        pin=input("Enter pin to deposit:")
        while k < len(customer_names)-1:
            k=k+1
            if name==customer_names[k]:
                if pin == customer_pins[k]:
                    deposit_amt=eval(input("Enter deposit amount:"))
                    deposit=deposit_amt+customer_amount[k]
                    balance=balance+deposit
                    print("Available balance is ",balance,end=" ")
                    print("/- Rs")
                    print("\nYou deposit successfully")
                    j=j+1
        if j < 1:
            print("Your name and pin doesn't match.Please try again")
            break

def withdraw_fun():
    x=0
    withdraw=0
    print("Selected option number",option)
    while x < 1:
        cus_name=input("Enter your name to withdraw:")
        cus_pin=input("Enter your pin to withdraw:")
        k=-1
        while k < len(customer_names)-1:
            k=k+1
            balance_amt=0
            if cus_name==customer_names[k]: 
                if cus_pin==customer_pins[k]:
                    withdraw_amt=eval(input("Enter withdraw amount:"))
                    if withdraw_amt > customer_amount[k]:
                        print("\nYour entered amount is exceeded")
                    else:
                        balance_amt=customer_amount[k]-withdraw_amt
                    print("\nAvailable amount is ",balance_amt,end=" ")
                    print("/- Rs")
                    print("Withdraw is successful")
                x=x+1
        if x < 1:
            print("Your name and pin doesn't match.Please try again")
            break

def balenquiry_fun():
    y=0
    print("Selected option number",option)
    while y < 1:
        cus_name=input("Enter your name for balance enquiry:")
        cus_pin=input("Enter your pin for balance enquiry:")
        print()
        k=-1
        while k < len(customer_names) -1 :
            k=k+1
            if cus_name == customer_names[k]:
                if cus_pin == customer_pins[k]:
                    print(datetime.now())
                    print("Branch Name : Anakapalli")
                    print("="*25)
                    print("Customer Name: ",end=" ")
                    print(customer_names[k])
                    print("Available Balance:",end=" ")
                    print(customer_amount[k],end=" ")
                    print("/- Rs")
                    y=y+1
        if y < 1:
            print("Your name and pin doesn't match.Please try again")
            break
def cuslist_fun():
    print("Selected option number",option)
    k=0
    print("Customer names and balances are mentioned below:")
    while k < len(customer_names):
        print("\nCustomer names:",customer_names[k])
        print("Customer balances:",customer_amount[k],end=" ")
        print("/-Rs")
        k=k+1

def closeAnt_fun():
    z=0
    print("Selected option number",option)
    while z < 1:
        cus_name=input("Enter your name to remove account:")
        cus_pin=input("Enter your pin to remove account:")
        a=-1
        while a < len(customer_names) - 1:
            a=a+1
            if cus_name == customer_names[a]:
                if cus_pin == customer_pins[a]:
                    customer_names.remove(customer_names[a])
                    customer_pins.remove(customer_pins[a])
                    print("\n---- Your account is successfully removed ----")
                    z=z+1
        if z < 1:
            print("Your name and pin doesn't match.Please try again")
            break
def modify_fun():
    m=0
    while m < 1:
        cus_name=input("Enter your name to modify your account:")
        cus_pin=input("Enter your pin to modify your account:")
        f=-1
        while f < len(customer_names) - 1:
            f=f+1
            if cus_name == customer_names[f]:
                if cus_pin == customer_pins[f]:
                    new_name=input("Enter your name to modify:")
                    new_pin=input("Enter your new pin to modify:")
                    customer_names[f]=new_name
                    customer_pins[f]=new_pin
                    print(customer_names,customer_pins)
                    print("---- Your account is successfully modified ----")
                    m=m+1
        if m < 1:
            print("Your name and pin doesn't match.Please try again")
def exit_fun():
    print("Selected option number",option)
    print("\nThank you for visiting our Moon Bank")
    print("Have a nice day")

while True:
    print('''
    1. Open a new account
    2. Deposit 
    3. Withdraw
    4. Balance Enquiry
    5. All account holder list
    6. Close bank account
    7. Modify bank account
    8. Exit
    ''')
    option=int(input("Enter your option:"))
    if option==1:
        NewAccount()
        print("To continue further select other options")
    elif option == 2:
        deposit_fun()
        print("To continue further select other options")
    elif option == 3:
        withdraw_fun()
        print("To continue further select other options")
    elif option == 4:
        balenquiry_fun()
        print("To continue further select other options")
    elif option == 5:
        cuslist_fun() 
        print("To continue further select other options") 
    elif option == 6:
        closeAnt_fun()
        print("To continue further select other options")
    elif option == 7:
        modify_fun()
    elif option == 8:
        exit_fun()
        break
    else:
        print("Please enter valid option")
        break





        
                    


    
                        
                

                



        


