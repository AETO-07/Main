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
    try:
        ask_choice = int(input("Enter your choice: "))

        if ask_choice >= 1 and ask_choice <=8:
            return ask_choice
        else:
            print("Enter any digit from 1-8.")
    except ValueError:
        print("Invalid input!")
        
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

    elif save_choice == 5:
        try:
            request_sender_account = int(input("Enter Sender's account number: "))

        except ValueError:
            print("Invalid Input")
            continue
            
        verify_sender_account = find_account(request_sender_account)

        if verify_sender_account is None:
            print("Account not found!")
            continue

        print(verify_sender_account)

        try:
            request_recipient_account = int(input("Enter Recipient's account number: "))

        except ValueError:
            print("Invalid input!")
            continue

        verify_recipient_account = find_account(request_recipient_account)

        if verify_recipient_account is None:
            print("Account not found!")
            continue
        
        print(verify_recipient_account)

        if request_sender_account == request_recipient_account:
            print("Sender and recipient accounts cannot be the same.")
            continue

        try: 
            request_amount = float(input("Enter transfer amount: ").replace(",", ""))

        except ValueError:
            print("Invalid input!")
            continue

        confirm_transaction = input(f"Are you sure you want to transfer {request_amount:,.2f} to {request_recipient_account}? (y/n): ")
        if confirm_transaction.lower() == "y":
            verify_amount = verify_sender_account.withdraw(request_amount)
            if verify_amount:
                verify_recipient_account.deposit(request_amount)
                print("Transfer successful!")
                print(verify_sender_account)
                print(verify_recipient_account)

        elif confirm_transaction.lower() == "n":
            print("Transfer cancelled.")


        