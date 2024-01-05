import random


class BankAccount:
    def __init__(self, account_number, balance, account_holder_name):
        self.account_number = account_number
        self.balance = balance
        self.account_holder_name = account_holder_name

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount} into account {self.account_number}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        print(f"Withdrew ${amount} from account {self.account_number}")

    def check_balance(self):
        print(f"Account {self.account_number} has ${self.balance}")

    def transfer_funds(self, to_account, amount):
        try:
            self.withdraw(amount)
            to_account.deposit(amount)
            print(
                f"Transferred ${amount} from account {self.account_number} to account {to_account.account_number}"
            )
        except ValueError as e:
            print(e)

    def __repr__(self):
        return f"Account {self.account_number} has ${self.balance}"


def main():
    account = create_account()
    account.deposit(50)
    account.withdraw(25)
    account.check_balance()

    try:
        account.withdraw(1000)
    except ValueError as e:
        print(e)

    print(account)

    friends_account = BankAccount(generate_account_number(), 100, "Friend")

    account.transfer_funds(friends_account, 10)
    account.check_balance()
    friends_account.check_balance()


def create_account():
    account_number = generate_account_number()
    balance = 0
    account_holder_name = input("Enter your name: ")
    return BankAccount(account_number, balance, account_holder_name)


def generate_account_number():
    return random.randint(1000, 9999)


if __name__ == "__main__":
    main()
