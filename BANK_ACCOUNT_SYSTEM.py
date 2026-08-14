class BankAccount:
    def __init__(self, account_name, account_number):
        self.account_name = account_name
        self.balance = 0.0
        self.account_number = account_number
        self.history = []


    def __str__(self):
        return (
            f"Account Name: {self.account_name} | "
            f"Account_No: {self.account_number} | "
            f"Balance: {self.balance:,.2f}"
        )