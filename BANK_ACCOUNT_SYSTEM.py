import json, datetime
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

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return False    
        
        self.balance += amount
        self.history.append({"type": "Deposit",
                            "amount": amount,
                            "date": datetime.datetime.now().strftime("%d %b, %Y")
                            })
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return False

        if amount <= self.balance:
            self.balance -= amount
            self.history.append({
                "type": "Withdrawal",
                "amount": amount,
                "balance": self.balance,
                "date": datetime.datetime.now().strftime("%d %b, %Y")
            })
            return True
        else:
            print(
                'Insufficient funds. Withdrawal amount exceeds available balance.'
            )
            return False

accounts = []
next_account_number = 1000000


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

def find_account(account_number):
    for account in accounts:
        if account.account_number == account_number:
            return account
        
    return None
            
while True:
    save_choice = menu()
    if save_choice == 1:
        account_name = input("Enter account name: ")
        if account_name.strip() == "":
            print("Account name cannot be empty.")
            continue
        account_number = next_account_number
        next_account_number += 1

        user = BankAccount(account_name, account_number)
        accounts.append(user)
        print(f"Account created successfully!")
        print(user)

        deposit_request = input("Would you like to make an initial deposit now? (y/n): ")

        if deposit_request.lower() == "y":
            user_amount = float(input("Enter deposit amount: ").replace(",", ""))
            if user.deposit(user_amount):
                print("Initial deposit successful!")
                print(user)
        elif deposit_request.lower() == "n":
            pass
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")
            #I feel it should ask the question again

    elif save_choice == 2:
        if not accounts:
            print("No accounts found.")
        else:
            for account in accounts:
                print(account)

    elif save_choice == 3:
        try:
            ask_account_number = int(input("Enter account number: "))
        except ValueError:
            print("Invalid input. Please enter a valid account number.")
            continue

        account = find_account(ask_account_number)
        if account is None:
            print("Account not found.")
            continue

        print(account)
        
        try:
            ask_deposit_amount = float(input("Enter deposit amount: ").replace(",", ""))
            save_deposit = account.deposit(ask_deposit_amount)
            if save_deposit:
                print("Deposit Successful!")
                print(account)

        except ValueError: 
            print("Invalid input. Please enter a valid amount.")

    elif save_choice == 4:
        try:
            ask_account_number = int(input("Enter account number: "))

        except ValueError:
            print("Invalid input.")
            continue

        account = find_account(ask_account_number)
        if account is None:
            print("Account not found.")
            continue

        print(account)
    
        try:
            withdraw_amount = float(input("Enter withdrawal amount: ").replace(",", ""))
        except ValueError:
            print("Invalid input!")
            continue

        confirm = input(f"Are you sure you want to withdraw ₦{withdraw_amount:,.2f}? (y/n): ")
        if confirm.lower() == "y":
            proceed_withdrawal = account.withdraw(withdraw_amount)
            if proceed_withdrawal:
                print("Withdraw successful!")
                print(account)

        elif confirm.lower() == "n":
            print("Withdrawal cancelled.")
        
