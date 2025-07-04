from expense_types import SimpleExpense
from file_utils import load_expenses, save_expense

FILENAME = "expenses.txt"

def show_menu():
    print("\n Expense Tracker Menu")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Summary by Category")
    print("4. Exit")

def add_expense():
    desc = input("Enter description: ")
    try:
        amt = float(input("Enter amount: $"))
    except ValueError:
        print("Invalid amount. ")
        return
    cat = input("Enter Category: ")
    expense = SimpleExpense(desc, amt, cat)
    save_expense(FILENAME, expense)
    print("Expense saved!")

def view_expenses():
    data = load_expenses(FILENAME)
    if not data:
        print("No expenses recorded")
        return
    print("\n Expense Entries")
    for desc, amt, cat in data:
        print(f"• {desc} - ${amt:.2f} [{cat}]")

def show_summary():
    data = load_expenses(FILENAME)
    totals = {}
    overall = 0
    for _, amt, cat in data:
        totals[cat] = totals.get(cat, 0) + amt
        overall += amt
    print("\n Expense Summary by category: ")
    for cat, total in totals.items():
        print(f"*{cat}: ${total:.2f}")
    print("Total spend: $", round(overall, 2))

def run():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    run()
