class Account:
    def __init__(self, acc_number, opening_balance):
        self.__acc_number = acc_number
        self.__balance = opening_balance

    def deposit(self, sum_amount):
        if sum_amount > 0:
            self.__balance += sum_amount
            print("Amount deposited:", sum_amount)
        else:
            print("Invalid amount.")

    def withdraw(self, sum_amount):
        if 0 < sum_amount <= self.__balance:
            self.__balance -= sum_amount
            print("Amount withdrawn:", sum_amount)
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance

    def display(self):
        print("Account Number:", self.__acc_number)
        print("Balance:", self.__balance)


class SavingsAccount(Account):
    def add_interest(self, interest_rate):
        accrued = self.get_balance() * interest_rate / 100
        self.deposit(accrued)
        print("Interest added:", accrued)


class CurrentAccount(Account):
    def withdraw(self, sum_amount):
        if sum_amount <= self.get_balance() + 5000:
            super().withdraw(sum_amount)
        else:
            print("Overdraft limit exceeded.")


print("----- Savings Account -----")
savings = SavingsAccount("S101", 10000)
savings.display()
savings.deposit(2000)
savings.withdraw(1000)
savings.add_interest(5)
savings.display()

print("\n----- Current Account -----")
current = CurrentAccount("C101", 5000)
current.display()
current.deposit(3000)
current.withdraw(7000)
current.display()
