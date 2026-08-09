import hashlib
import json
import time

class Block:
    def __init__(self, index, previous_hash, transactions):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash
        }, sort_keys=True).encode()

        return hashlib.sha256(data).hexdigest()


class TilimikoBlockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", [])

    def add_block(self, transactions):
        previous = self.chain[-1]
        new_block = Block(
            len(self.chain),
            previous.hash,
            transactions
        )
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False

            if current.previous_hash != previous.hash:
                return False

        return True


if __name__ == "__main__":
    tilimiko = TilimikoBlockchain()

    tilimiko.add_block({
        "from": "Alice",
        "to": "Bob",
        "amount": 10
    })

    print("Tilimiko blockchain started!")
    print("Blocks:", len(tilimiko.chain))
    print("Blockchain valid:", tilimiko.is_valid())

    for block in tilimiko.chain:
        print(block.index, block.hash)
