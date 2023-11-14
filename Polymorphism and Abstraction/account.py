class Account:
    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []
        self.account_balance = 0

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self._transactions.append(amount)
        self.account_balance += amount

    @property
    def balance(self):
        self.account_balance = sum(self._transactions) + self.amount
        return self.account_balance

    def _transactions(self):
        return self

    @staticmethod
    def validate_transaction(account, amount_to_add):
        balance = account.balance
        if balance + amount_to_add < 0:
            raise ValueError('sorry cannot go in debt!')
        account.add_transaction(amount_to_add)
        return f'New balance: {account.account_balance}'

    def __add__(self, other):
        names = f'{self.owner}&{other.owner}'
        amounts = self.amount + other.amount
        result = Account(names, amounts)
        result._transactions = self._transactions + other._transactions
        result.account_balance = self.account_balance + other.account_balance
        return result

    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __ne__(self, other):
        return self.balance != other.balance


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))

acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)

print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)


