# expense_manager.py

FILE_NAME = "expense_manager.txt"


# Function to add an expense
def add_expense(date, category, amount, note):

    file = open(FILE_NAME, "a")

    record = date + "," + category + "," + str(amount) + "," + note + "\n"

    file.write(record)

    file.close()

# Function to read all expenses
def get_expenses():

    expenses = []


    try:
        file = open(FILE_NAME,"r")

        for line in file:

            data = line.strip().split(",")

            expense = {
                "date": data[0],
                "category": data[1],
                "amount": float(data[2]),
                "note": data[3]
            }

            expenses.append(expense)

        file.close()

    except:
        pass

    return expenses


# Function to calculate total expenses
def total_expenses():
    expenses = get_expenses()
    total = 0
    for e in expenses:
        total += e["amount"]
    return total

# Function for category wise expenses
def category_wise_expenses():
    expenseee = get_expenses()
    category_data = {}
    for e in expenses:

        category = e["category"]
        amount = e["amount"]

        if category in category_data:
            category_data[category] = category_data[category] + amount
        else:
            category_data[category] = amount

    return category_data
