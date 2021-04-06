from datetime import date
import time
import sys
import random

time = (time.strftime("%H:%M:%S"))
date = date.today()
balance = 100000
database ={}


def init():
    try:
        print("********** welcome to MY-ATM app **********\n")

        existingCustomer = int(input("New Customer (1) Existing customer (2)\n>"))

        if existingCustomer == 1:
            register()
        if existingCustomer == 2:
            print("login")
        else:
            print("Invalid selection")
            init()
    except ValueError:
        print("invalid selection\n")
        init() 


def register():
    print("************ Proceed with registration ************")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    accountNumber = accountNumberGenerator()
    
    database[accountNumber] = [first_name,last_name,email,password]

    print("registration successful\n")
    print("your account number is: %d\n" %accountNumber)
    login()


def login():
    password_count = 0
    while password_count <=2:
            
        print ("**** login ****\n")

        accountNumberByUser = int(input("Enter Account Number: "))
        passwordByUser = input("Enter password: ")
        

        for accountnumber, userDetails in database.items():
            if accountNumberByUser == accountnumber:
                if passwordByUser == userDetails[3]:
                    welcome(userDetails)
             
        password_count += 1            
        print("invalid username or password entered\n")
        #login()

    sys.exit("Too many tries, Try again later")


def welcome(user):
    print("********* Welcome %s %s ********\n" %(user[0],user[1]))
    decision()    




def decision():
    #while True:
        try:
            options = int(input("select: (1) withdraw (2) deposit (3) complaint (4) Exit\n> "))
            if (options == 1):
                withdraw()
            elif(options == 2):
                deposit()
            elif(options == 3):
               complaint()
            elif options == 4:
                exit(0)
            else:
                print("Invalid selection")
                #decision()
        except ValueError:
            print("invalid entry, integer only")
            #decision()
        #except Exception:
            #print("something went wrong")


def withdraw():
    try:
        print("How much will you like to withdraw?")
        amt =int(input(">"))
        if amt > balance:
            print("Invalid transaction, withdraw amount is greater than balance")
            withdraw()
        else:
            new_balance = balance - amt
            print("Take your cash %d" %amt)
            print("New balance after withdrawal = %d" %new_balance)
            additional_decision()
            #exit(0)
    except ValueError:
            print("invalid entry, integer only")    
            withdraw()






def deposit():
    print("How much would you like to deposit?")
    amt = int(input("> "))
    new_deposit_balance = balance + amt
    print("Deposit successful")
    print("New balance = %d" %new_deposit_balance)
    additional_decision()

def complaint():
    print("What issue will you like to report")
    report = input("Enter your complaint : \n>")
    if report !="":
        print("Complaint received,Thank you for contacting us")
        exit(0)
    else:
        print ("no complaint entered,Thank you for contacting us")
        exit(0)

def accountNumberGenerator():
    return random.randrange(1111111111,9999999999)

def additional_decision():
    addDisc=input("would you like to perform an additon task  Y or N\n>")
    more_decision = addDisc.upper()
    if more_decision == 'Y':
        decision()
    elif more_decision == 'N':
        print("Thank you for banking with us")
        exit(0)
    else:
        print("make an appropriate selection")
        additional_decision()


init()


#print(accountNumberGenerator())
