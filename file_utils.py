import os

def load_expenses(filename):
    expenses = []
    if not os.path.exists(filename):
        return expenses
    else:
        print("Error: File not found")
    
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line: 
                continue
            try: 
                parts = line.split(" - ")
                if len(parts) != 2:
                    raise ValueError("Line does not split into 2 parts")
                description = parts[0]
                amount_part, category_part = parts[1].split(" [")
                raw_amount = amount_part.replace("$", "").strip()
                category = category_part.strip("] \n")

                expenses.append((description, float(raw_amount), category))
            except Exception:
                print(f"Skipped malformed line: {line}")
    return expenses

def save_expense(filename, expense_obj):
    with open(filename, "a") as file: 
        file.write(expense_obj.describe() + "\n")