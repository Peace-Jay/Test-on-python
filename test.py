class Customers:
    def __init__(self, customer_name, customer_account):
        self.name = customer_name
        self.number = customer_account
        self.balance = 0


    def display_balance(self):
        print("The account balance for", self.name, "is:", self.balance)

    def add_money(self, amount):
        self.balance += amount
        print(amount, "added to", self.name, "'s account.", "New balance:", self.balance)

    def transfer_money(self, other_user, amount):
        if amount <= self.balance:
            self.balance -= amount
            other_user.balance += amount
            print(amount, "transferred from", self.name, "to", other_user)
            print(self.name, "'s New balance:", self.balance)
        else:
            print("Insufficient funds.", self.name, "'s balance:", self.balance)


class Bank:
    def __init__(self):
        self.users = []


    def register_user(self, name):
        customer_account = len(self.users) + 1
        new_customers = Customers(name, customer_account)
        self.users.append(new_customers)
        print("user", name, "registered with account number", customer_account)


    def display_users(self):
        for user in self.users:
            print(user)
if __name__ == "__main__":
    bank_instance = Bank()


    while True:
        print("\nBanking System")
        print("1. Register System")
        print("2. Display Users")
        print("3. View Account Balance")
        print("4. Add Money to Account")
        print("5. Transfer Money")
        print("6. Exit")


        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            name = input("Enter your name:")
            bank_instance.register_user(name)
            print("this works")
        elif choice == "2":
            bank_instance.display_users()
        elif choice == "3":
            user_number = int(input("Enter your account number:"))
            user = bank_instance.users[user_number - 1]
            user.display_balance()
        elif choice == "4":
            user_number = int(input("Enter your account number:"))
            user = bank_instance.users[user_number - 1]
            amount = float(input("Enter the amount to add:"))
            user.add_money(amount)
        elif choice == "5":
            sender_number = int(input("Enter your account number: "))
            receiver_number = int(input("Enter the receiver's account number: "))
            sender = bank_instance.users[sender_number - 1]
            receiver = bank_instance.users[receiver_number - 1]
            amount = float(input("Enter the amount to transfer: "))
            sender.transfer_money(receiver, amount)
        elif choice == "6":
            print("Exiting the banking system. Goodbye!")
        else:
            print("Invalid choice. Please enter a valid option")
