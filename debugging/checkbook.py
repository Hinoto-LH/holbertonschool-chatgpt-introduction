class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        self.show_balance()

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
            return
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}")
        self.show_balance()

    def show_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")


def get_amount(prompt):
    try:
        amount = float(input(prompt))
        return amount
    except ValueError:
        print("Please enter a valid number.")
        return None


def main():
    cb = Checkbook()

    while True:
        action = input(
            "\nWhat would you like to do? (deposit, withdraw, balance, exit): "
        ).lower()

        if action == "exit":
            print("Goodbye!")
            break

        elif action == "deposit":
            amount = get_amount("Enter the amount to deposit: $")
            if amount is not None:
                cb.deposit(amount)

        elif action == "withdraw":
            amount = get_amount("Enter the amount to withdraw: $")
            if amount is not None:
                cb.withdraw(amount)

        elif action == "balance":
            cb.show_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
