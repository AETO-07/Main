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
            f"Balance: ₦{self.balance:,.2f}"
        )

accounts = []

def menu():
    print(
        "WELCOME TO BANK ACCOUNT SYSTEM" \
        "\n 1. Create Account" \
        "\n 2. View Accounts" \
        "\n 3. Deposit" \
        "\n 4. Withdraw" \
        "\n 5. Transfer" \
        "\n 6. View Transaction History" \
        "\n 7. Save Accounts" 
        "\n 8. Exit"
    )

    ask_choice = int(input("Enter your choice: "))
    return ask_choice

while True:
    save_choice = menu()
