from atm import Atm

class AtmController:
    def __init__(self):
        self.atm = Atm()


    def get_number(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print('Enter a valid number')


    def display_menu(self):
        print('\nWelcome to the ATM!')
        print('1. Check Balance')
        print('2. Deposit')
        print('3. Withdrawal')
        print('4. Exit')


    def check_balance(self):
        balance = self.atm.check_balance()
        print(f'Your current balance is ${balance}')


    def deposit(self):
        while True:
            try:
                deposit_amount = self.get_number('Enter the amount to deposit: ')
                self.atm.deposit(deposit_amount)
            
                print(f'Successfully deposited ${deposit_amount}')
                break
            except ValueError as error:
                print(error)


    def withdraw(self):
        while True:
            try:
                withdrawal_amount = self.get_number('Enter the amount to withdraw: ')
                self.atm.withdraw(withdrawal_amount)

                print(f'Successfully withdrew ${withdrawal_amount}')
                break
            except ValueError as error:
                print(error)
                

    def run(self):
        while True:
            self.display_menu()

            choice = input('Please choose an option: ')
            match choice:
                case '1':
                    self.check_balance()

                case '2':
                    self.deposit()

                case '3':
                    self.withdraw()

                case '4':
                    print('Thank you for using the ATM')
                    break

                case _:
                    print('Invalid choice. Please try again')