import datetime
class Expense:
    def __init__(self, category, amount, name, date):
        self.category = category
        self.amount = amount
        self.name = name
        self.date = date

    def __str__(self):
        return f"Your Expense is: {self.category} | {self.amount} | {self.name} | {self.date}"

# expense = Expense("Cereals", 2500, "Chinese-rice", "2023-06-01")
# print(expense)

expenses = []

def menu():
    print("WELCOME TO EXPENSE TRACKER" \
          "\n 1. Add Expense" \
          "\n 2. View Expenses" \
          "\n 3. Search Expense" \
          "\n 4. Edit Expense" \
          "\n 5. Delete Expense" \
          "\n 6. Show total spending" \
          "\n 7. Save Expenses" \
          "\n 8. Exit"
          )

    choice = int(input("Enter your choice: "))
    return choice

while True:

    saveChoice = menu()

    if saveChoice == 1:
        category = input("Enter expense's category: ")
        amount = float(input("Enter expense's amount: "))
        name = input("Enter expense's name: ")
        date = datetime.datetime.now().strftime("%d %b, %Y")

        data = Expense(category, amount, name, date)
        expenses.append(data)
        print("Expense added successfully!")

    elif saveChoice == 2:
        if len(expenses) == 0:
            print("No expenses found.")
        else: 
            print("Your Expenses: ")
            for ex in expenses:
                print(ex)

    elif saveChoice == 3:
        search_name = input("Enter expense's name to search: ")
        found = False
        for ex in expenses:
            if ex.name.lower() == search_name.lower():
                print(ex)
                found = True
        if not found:
                print("Expense not found!")
                


    