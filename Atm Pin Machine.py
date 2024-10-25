import time

print('''Welcome to Bank of India
---------------------------
Please insert your  ATM CARD..''')

time.sleep(5)

password = 2003

pin = int(input("Please Enter your Atm Pin:"))
balance = 5000

if pin == password:

    while True:
        print('--------------------------------------')
        print('''
        1 == Balance Enquiry
        2 == Withdraw Amount
        3 == Deposite Amount
        4 == Exit
        ''')
        print('--------------------------------------')
        try:
            option = int(input('Plese choose correct option: '))
            print('--------------------------------------')
        except:
            print("Please Enter valid option..")

        if option == 1:
            print(f'Your current balance is {balance}')

        if option == 2:
            d_amount = int(input('Enter your amount:'))

            with_amount = balance - d_amount

            print(f'{d_amount} amount is debited from your account')

            print(f'Your updated balance is {with_amount}')

        if option == 3:
            c_amount = int(input('Enter your amount:'))

            dep_amount = balance + c_amount

            print(f'{c_amount} amount is credited from your account')

            print(f'Your updated balance is {dep_amount}')

        if option == 4:
            print('''Your transaction is successfully completed
            Thankyou visit again''')
            break

else:
    print('You Enter wrong pin, please try again..')
