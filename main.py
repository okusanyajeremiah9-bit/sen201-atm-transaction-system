class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


class ATM:
    def deposit(self, account, amount):
        account.balance += amount

    def withdraw(self, account, amount):
        if amount <= account.balance:
            account.balance -= amount
        else:
            print("Insufficient balance")

    def display_balance(self, account):
        print(f"Account Owner: {account.owner}")
        print(f"Balance: {account.balance}")


def main():
    account = Account("Fortune", 1000)
    atm = ATM()

    atm.deposit(account, 500)
    atm.withdraw(account, 300)
    atm.display_balance(account)


if __name__ == "__main__":
    main()
