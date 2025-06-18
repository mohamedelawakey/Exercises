from learn import BankAccount

account1 = BankAccount("Ali", 12000, "Savings")
print(account1)
print("Tax:", account1.calculate_tax())

account2 = BankAccount("Sara", 8000, "Checking")
account2.deposit(2000)
print(account2)
print("Total accounts:", BankAccount.get_total_accounts())
