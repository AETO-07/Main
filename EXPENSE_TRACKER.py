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