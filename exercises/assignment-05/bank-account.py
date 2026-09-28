'''
Task-1: BankAccount System
1. Create a Python class named BankAccount.
2. Define the following methods within the BankAccount class:
	set_account_details(self, account_number, account_holder_name, initial_balance=0)
	deposit(self, amount)
	withdraw(self, amount)
	display_account_info(self)

3. Create an object of the BankAccount class.
4. Use the set_account_details method to set the account number, account holder's name, and initial balance.
5. Use the deposit and withdraw methods to simulate depositing and withdrawing money from the account.
6. Finally, use the display_account_info method to print the account details.
'''
class BankAccount:
    account_number=0
    account_holder_name=""
    amount=0

    def set_account_details(self, account_number, account_holder_name, initial_balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit amount: ", amount)
            print("New balance: ", self.balance)
            print("--------------------------------")
        else:
            print("Enter a valid amount")
            print("--------------------------------")
            
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdraw amount: ", amount)
            print("New balance: ", self.balance)
            print("--------------------------------")
        else:
            print("Invalid! Not enough balance available")
            print("--------------------------------")

    def display_account_info(self):
        print("Account Holder Name: ", self.account_holder_name)
        print("Account Number: ", self.account_number)
        print("Balance: ", self.balance)
        print("--------------------------------")

user1=BankAccount()
user1.set_account_details(account_number=123456789101, account_holder_name="Mohiuddin", initial_balance=500)
user1.deposit(amount=15000)
user1.withdraw(amount=5000)
user1.display_account_info()