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

        current = self.get_balance(address)
        self.balances[address] = current + amount

    def subtract_balance(self, address, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")

        current = self.get_balance(address)

        if amount > current:
            raise ValueError("Insufficient balance")

        self.balances[address] = current - amount


if __name__ == "__main__":
    state = BlockchainState()

    state.set_balance("Alice", 100)
    state.subtract_balance("Alice", 30)
    state.add_balance("Bob", 30)

    print("Tilimiko state system started!")
    print("Alice balance:", state.get_balance("Alice"))
    print("Bob balance:", state.get_balance("Bob"))
