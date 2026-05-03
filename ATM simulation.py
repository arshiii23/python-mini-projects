class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt
        print("Deposited:", amt)

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            print("Withdrawn:", amt)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Balance:", self.balance)


name = input("Enter your name: ")
balance = float(input("Enter initial balance: "))
account = BankAccount(name, balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amt = float(input("Enter Amount: "))
        account.deposit(amt)

    elif choice == "2":
        amt = float(input("Enter Amount: "))
        account.withdraw(amt)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        break

    else:
        print("Invalid choice")