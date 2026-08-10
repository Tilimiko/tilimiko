import json
from wallet import Wallet


class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = None

    def to_dict(self):
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount
        }

    def signing_data(self):
        return json.dumps(self.to_dict(), sort_keys=True)

    def sign(self, wallet):
        self.signature = wallet.sign(self.signing_data())

    def is_signed(self):
        return self.signature is not None


if __name__ == "__main__":
    sender_wallet = Wallet()

    transaction = Transaction(
        sender="sender-public-key",
        recipient="recipient-public-key",
        amount=10
    )

    transaction.sign(sender_wallet)

    print("Tilimiko transaction created!")
    print("Amount:", transaction.amount)
    print("Signed:", transaction.is_signed())
