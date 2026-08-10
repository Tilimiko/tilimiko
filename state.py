class BlockchainState:
    def __init__(self):
        self.balances = {}

    def get_balance(self, address):
        return self.balances.get(address, 0)

    def set_balance(self, address, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")

        self.balances[address] = amount

    def add_balance(self, address, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")

        self.balances[address] = self.get_balance(address) + amount

    def subtract_balance(self, address, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")

        if amount > self.get_balance(address):
            raise ValueError("Insufficient balance")

        self.balances[address] = self.get_balance(address) - amount

    def apply_transaction(self, transaction):
        if not transaction.is_valid(self):
            raise ValueError("Invalid transaction")

        self.subtract_balance(transaction.sender, transaction.amount)
        self.add_balance(transaction.recipient, transaction.amount)


if __name__ == "__main__":
    state = BlockchainState()

    state.set_balance("Alice", 50)

    print("Before transaction:")
    print("Alice balance:", state.get_balance("Alice"))
    print("Bob balance:", state.get_balance("Bob"))
