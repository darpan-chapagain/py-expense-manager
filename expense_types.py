from base_entry import ExpenseEntry

class SimpleExpense(ExpenseEntry):
    def describe(self):
        return f"{self.get_description()} - ${self.get_amount():.2f} [{self.get_category()}]"
    