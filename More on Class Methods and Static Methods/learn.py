class BankConfig:
    TAX_RATE = 0.05
    MIN_BALANCE_FOR_TAX = 10000
    
class BankAccount:
    total_accounts = 0
        
    def __init__(self, owner_name, balance, account_type):
        self.owner_name = owner_name
        self.balance = balance
        self.account_type = account_type
        BankAccount.total_accounts += 1
        
        if balance < 0:
            raise ValueError("Initial balance can't be negative")
        if not owner_name:
            raise ValueError("Owner name can't be empty")
    
    @classmethod  
    def get_total_accounts(cls):
        return cls.total_accounts
    
    @property
    def acc_type(self):
        return self.account_type
    
    def deposit(self, add_to_balance):
        if add_to_balance > 0 :
            self.balance += add_to_balance
            return True
        else:
            return False

    def withdraw(self, remove_to_balance):
        if remove_to_balance > 0 and remove_to_balance <= self.balance:
            self.balance -= remove_to_balance
        else:
            return "Insufficient funds"
        
    @property
    def final_balance(self):
        return self.balance
    
    def calculate_tax(self):
        if self.balance >= BankConfig.MIN_BALANCE_FOR_TAX and self.account_type == 'Savings':
            return self.final_balance * BankConfig.TAX_RATE
        else:
            return 0
    
    def __str__(self):
        return f"{self.owner_name} - {self.acc_type} - Balance: ${self.balance:.2f}"