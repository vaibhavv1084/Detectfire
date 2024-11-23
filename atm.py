class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

def display_menu():
    print("\nATM Simulator")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def main():
    atm = ATM()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print(f"Your current balance is: ${atm.check_balance():.2f}")
        
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            if atm.deposit(amount):
                print(f"${amount:.2f} deposited successfully.")
            else:
                print("Invalid deposit amount.")
        
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            if atm.withdraw(amount):
                print(f"${amount:.2f} withdrawn successfully.")
            else:
                print("Invalid or insufficient funds for withdrawal.")
        
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
