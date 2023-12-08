from time import sleep
class Customers:
    def __init__(self, customer_name, customer_account):
        self.name = customer_name
        self.number = customer_account
        self.balance = 0
#The self.name, self.number is used to call out the functions in the def __init__ for it to be useful in the remaining code

    def display_balance(self):
        print("The account balance for", self.name, "is:", self.balance)
#The display_balance is used make it known that we want to extract a balance for a particular customer

    def add_money(self, amount):
        self.balance += amount
        print(amount, "added to", self.name, "'s account.", "New balance:", self.balance)
#The add_money function is used to know the amount to be account(amount); for the self.balance += amount is for it to be adding to to the initial self.balance which is 0

    def transfer_money(self, other_user, amount):
        if amount <= self.balance:
            self.balance -= amount
            other_user.balance += amount
            print(amount, "transferred from", self.name, "to", other_user)
            print(self.name, "'s New balance:", self.balance)
        else:
            print("Insufficient funds.", self.name, "'s balance:", self.balance)
# The transfer_money function is used to know the account you are transferring to(other_user) and the amount to be transferred to the new account(amount)


class Bank:
    def __init__(self):
        self.users = []
#

    def register_user(self, name):
        customer_account = len(self.users) + 1
        new_customers = Customers(name, customer_account)
        self.users.append(new_customers)
        print("user", name, "registered with account number", customer_account)
#The register_user function is used to get the name of the new customers that are about to register

    def display_users(self):
        for user in self.users:
            print(user.number, user.name, user.balance)
#The display user is to get the names and account number of people that have registered with the bank
if __name__ == "__main__":
    bank_instance = Bank()


    while True:
        print("**************PEACE BANK*************")
        print("*********WELCOME, WHAT DO YOU WANT TO DO TODAY*******")
        print("\nBanking System")
        print("1. Register User")
        print("2. Display Users")
        print("3. View Account Balance")
        print("4. Add Money to Account")
        print("5. Transfer Money")
        print("6. Exit")
        print("************************************")
        print("************************************")
#The above print statements is used to display the services we render in the bank

        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            name = input("Enter your name:")
            print("********************************************************")
            bank_instance.register_user(name)
            print("****************************************************")
#When the customer picks 1, he will be asked his name which will be immediately appended to the list with his account no
        elif choice == "2":
            bank_instance.display_users()
#when 2 is entered it is just for us to know the list of customers that have been registered
        elif choice == "3":
            user_number = int(input("Enter your account number:"))
            user = bank_instance.users[user_number - 1]
            user.display_balance()
#when 3 is entered it is for us to check his account balance by asking for his account number
        elif choice == "4":
            user_number = int(input("Enter your account number:"))
            user = bank_instance.users[user_number - 1]
            amount = float(input("Enter the amount to add:"))
            user.add_money(amount)
# when 4 is entered it is used to get account number(user_number) and to add amount to be transferred to the persons balance(amount)
        elif choice == "5":
            sender_number = int(input("Enter your account number: "))
            receiver_number = int(input("Enter the receiver's account number: "))
            sender = bank_instance.users[sender_number - 1]
            receiver = bank_instance.users[receiver_number - 1]
            amount = float(input("Enter the amount to transfer: "))
            sender.transfer_money(receiver, amount)
#When 5 is entered is to get thye account number you are transferring from(sender_number) and the account you are transferring to (receiver_number) and also the amount to be transferred
        elif choice == "6":
            print("Exiting the banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option")
        sleep(2)
# 6 is used when you are nog doing anything in the bank 1