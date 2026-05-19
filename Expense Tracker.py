expenses = []

while True:
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expenses.append({"name": name, "amount": amount})

    choice = input("Add another expense? (y/n): ")

    if choice.lower() != 'y':
        break

print("\nExpense Summary")

total = 0

for expense in expenses:
    print(f"{expense['name']} - ₹{expense['amount']}")
    total += expense['amount']

print(f"Total Expenses: ₹{total}")