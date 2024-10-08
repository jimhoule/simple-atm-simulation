# NOTE: All methods of a Class must have self has their first parameter
class Atm:
    # Initializer (initializes attributes)
    def __init__(self):
        self.balance = 0


    def check_balance(self):
        return self.balance
    

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit amount must be positive')
        
        self.balance += amount
        

    def withdraw(self, amount):
        if (amount <= 0):
            raise ValueError('Withdrawal amount must be positive')

        if (amount > self.balance):
            raise ValueError('Insufficient fund')
        
        self.balance -= amount