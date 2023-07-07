
class Bank:

    def __init__(self, initial_ammout=0.00):
        self.balance = initial_ammout

    def log_transaction(self, transaction_string):
        with open("transaction.txt", "a") as file:
            file.write(
                f"{transaction_string} \t\t\tBalance: {self.balance}\n")

    def read_transaction(self):
        with open("transaction.txt", "r") as file:
            print(file.read())

    def withdrawal(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            if (self.balance - amount < 0):
                print("You don't have money. ")
                self.log_transaction(f"Not enough money. Please add more.")
            else:
                self.balance = self.balance - amount
                self.log_transaction(f"Withdrew {amount}")

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance + amount
            self.log_transaction(f"Deposited {amount}")


account = Bank(50.50)

while True:
    
    try:
        transaction_history = input("Do you want to see your history transaction? (y/n) ")
        if transaction_history == "y":
            account.read_transaction()
            print("\n\n")
    except FileNotFoundError:
        print("The file is not created yet. Please have patience. ")
    except KeyboardInterrupt:
        break

    try:
        action = input("What kind of action do you want to take? (withdrawal/deposit) ")
    except KeyboardInterrupt:
        
        try:
            delete = input("Do you want to delete 'transaction.txt'? (y/n) ")
            if delete == "y":
                import os
                file = 'transaction.txt'  
                location = "D:\Programare\web_dev\Python\Python301\FinalProject"
                path = os.path.join(location, file)  
                os.remove(path)
        except FileNotFoundError:
            print("The file is not created yet. Please have patience. ")

        print("\nLeaving the ATM")
        break
    if action in ["withdrawal", "deposit"]:
        if action == "withdrawal":
            amount = input("How much do you want to take out? ")
            account.withdrawal(amount)
        else:
            amount = input("How much do you want to put in? ")
            account.deposit(amount)

        print(f"Your balance is {account.balance}")


    else:
        print("That is not a valid action. Try again.")
        continue
