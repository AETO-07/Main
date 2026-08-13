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

        optional_search = input("How would you like to search? (name / category): ")

        if optional_search.lower() == "name":
            search_name = input("Enter expense's name to search: ")
            found = False
            for ex in expenses:
                if search_name.lower() in ex.name.lower()  :
                    print(ex)
                    found = True
                    break
            if not found:
                print("Expense not found!")

        elif optional_search.lower() == "category":
            search_category = input("Enter expense's category to search: ")
            found = False
            for ex in expenses:
                if search_category.lower() == ex.category.lower()  :
                    print(ex)
                    found = True
                    break
            if not found:
                print("Expense not found!") 

    elif saveChoice == 4:
        expense_name = input("Enter the expense's name you want to edit: ") 
        found = False
        for ex in expenses:
            if expense_name.lower() == ex.name.lower():
                new_name = input("Enter new name: ")
                new_category = input("Enter new category: ")
                new_amount = float(input("Enter new amount: "))

                ex.name = new_name
                ex.category = new_category
                ex.amount = new_amount

                print("Expense updated successfully!")
                found = True
        if not found:
            print("Expense not found!")

    elif saveChoice == 5:
        delete_expense_name = input("Enter the expense's name you want to delete: ")
        found = False
        for ex in expenses:
            if delete_expense_name.lower() == ex.name.lower():
                confirm = input(f"Are you sure you want to delete the expense {ex.name}? (yes / no): ")
                if confirm.lower() == "yes":
                    expenses.remove(ex)
                    found = True
                    print("Expense deleted successfully!")
                    break
                elif confirm.lower() == "no":
                    print("Deletion cancelled.")
                    found = True
                    break
        if not found:
            print("Expense not found!")

    elif saveChoice == 6:
        total_amount = 0
        for ex in expenses:
            total_amount += ex.amount
        print(f'Total spending: {total_amount}')

        

            

        
                


    