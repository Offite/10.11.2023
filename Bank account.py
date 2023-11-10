class BankAccount:
    def init(self, customer, initial_balance):
     self.customer = customer
     self.balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Некорректное внесение средств")
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Недостаточно средств на счете")
        self.balance -= amount

