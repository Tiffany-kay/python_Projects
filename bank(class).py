#  code showing basic operation behind a bank
from datetime import datetime

class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = datetime.strptime(date_of_opening, "%d-%m-%Y").date()
        self.customer_name = customer_name

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit amount."
        self.balance += amount
        return f"Deposited {amount} in your account successfully. Your new balance is {self.balance}."

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount."
        if amount > self.balance:
            return "Insufficient balance. You can only withdraw up to your current balance."
        self.balance -= amount
        return f"Withdrawn {amount} from your account successfully. Your new balance is {self.balance}."

    def check_balance(self):
        return f"Your current balance is {self.balance}."

    def customer_details(self):
        return f"Customer name: {self.customer_name}\nAccount number: {self.account_number}\nAccount balance: {self.balance}\nAccount opening date: {self.date_of_opening}"

    def print_balance(self):
        print(self.check_balance())

    def print_details(self):
        print(self.customer_details())

# Example usage
bank_account = BankAccount(345556, 679098830000, "12-02-2021", "TIFFANY WANJIKU")
print(bank_account.deposit(40000))
print(bank_account.withdraw(50000))  # This will try to withdraw more than available balance
bank_account.print_balance()
bank_account.print_details()
