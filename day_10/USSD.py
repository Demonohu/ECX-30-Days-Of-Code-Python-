#USSD Bank Service
#Task: Create a mock USSD service that takes user input, and
#provides appropriate response. 
#Description:
#*User provides a USSD code as input.
#*User can then choose among a list of options(with numbers),
#whether to check balance, send money, purchase airtime, etc.
#*For check balance, the user is prompted to provide his 
# password (hard-coded by you.). If correct, s/he is shown 
#the balance-also hard coded.
#*For sending money, the user is prompted to choose from a
#selection of banks, after which he provides an account 
#number, and then an amount to send. And then a password, 
#which if correct, would send the required amount, and 
#deduct from account balance
#*Folllow a similar scheme as sending money, for 
#purchasing airtime-except that in this case, the user is
#prompted for a phone number instead.

from multiprocessing.sharedctypes import Value


class Bank:

    def __init__(self, balance, password):
        """This initializes the starting balance and the password."""
        self.__balance = balance
        self.__password = password


    def account_balance(self):
        passcode = input('\nEnter your password: ')
        if passcode == self.__password:
            print('\nYour balance is ₦', self.__balance, sep='')
        else:
            print('\nIncorrect password.')

    def transfer(self):
        banks = {1:'Access Bank', 2:'Eco Bank', 3:'Fidelity Bank', 4:'First Bank', 5:'GTB', 6:'Wema Bank', 7:'Zenith Bank'}
        print()
        for key, value in banks.items():
            print(str(key)+')', value)
        receiver_bank = input('\nSelect a bank. ')
        receiver_acct_no = int(input('Enter the account number: '))
        amount = float(input('Enter the amount: '))
        passcode = input("Enter your password: ")
        if passcode == self.__password:
            if self.__balance >= amount:
                print('\n₦', amount, ' has been sent to ', receiver_acct_no, ', ', receiver_bank, sep='')
                self.__balance -= amount
            else:
                print('\nInsufficient funds.')
        else:
            print('\nIncorrect password.')

    def airtime(self):
        isps = {1:'Airtel', 2:'Etisalat', 3:'Glo', 4:'MTN'}
        print()
        for key, value in isps.items():
            print(str(key)+')', value)
        isp = input('\nSelect an internet service provider.')
        amount = float('Enter the amount: ')
        number = input('Enter the number: ')
        passcode = input('Enter your password: ')
        if passcode == self.__password:
            if amount <= self.__balance:
                print('\n₦', amount, 'has been bought on ', number, ', ', isp, sep='')
                self.__balance -= amount
            else:
                print('\nInsufficient funds.')
        else:
            print("\nWrong password.")

        

def main():
    bal = float(input('Enter a starting balance: '))
    p_word = input('Enter a password: ')
    print()

    user = Bank(bal, p_word)
    operations = {1:'Check Balance', 2:'Send money', 3:'Send airtime'}
    while True:
        try:
            for key, value in operations.items():
                print(str(key)+')', value)
            operation= input('\nChoose an operation to perform: ')
            if int(operation) == 1:
                user.account_balance()
                break
            elif int(operation) == 2:
                user.transfer()
                break
            elif int(operation) == 3:
                user.airtime()
                break
            else:
                print('Invalid selection.')
                continue
            break
    
        except ValueError:
            print('Type the number of the operator to select.\n')
            continue

main()
       