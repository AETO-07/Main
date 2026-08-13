class Expense:
    def __init__(self, category, amount, name, date):
        self.category = category
        self.amount = amount
        self.name = name
        self.date = date

    def __str__(self):
        return f"Your Expense is: {self.category} | {self.amount} | {self.name} | {self.date}"

expense = Expense("Cereals", 2500, "Chinese-rice", "2023-06-01")
print(expense)

expenses = []

def menu():
    print("WELCOME TO EXPENSE TRACKER" \
          "\n 1. Add Expense" \
          "\n 2. View Expenses" \
          "\n 3. Search Expense" \
          "\n 4. Delete Expense" \
          "\n 5. Show total spending" \
          "\n 6. Save Expenses" \
          "\n 7. Exit"
          )

    choice = int(input("Enter your choice: "))
    return choice

saveChoice = menu()


    