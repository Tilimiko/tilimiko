import json
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from wallet import Wallet


class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = None
        self.public_key = None

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
        self.public_key = wallet.get_public_key()

    def is_valid(self, state=None):
        if self.signature is None or self.public_key is None:
            return False

        if not isinstance(self.amount, (int, float)) or self.amount <= 0:
            return False

        if not self.sender or not self.recipient:
            return False

        if state is not None:
            if self.sender == "sender-public-key":
                return False

            if state.get_balance(self.sender) < self.amount:
                return False

        try:
            public_key = serialization.load_pem_public_key(
                self.public_key
            )

            public_key.verify(
                self.signature,
                self.signing_data().encode(),
                ec.ECDSA(hashes.SHA256())
            )

            return True

        except Exception:
            return False


if __name__ == "__main__":
    sender_wallet = Wallet()

    transaction = Transaction(
        sender="Alice",
        recipient="Bob",
        amount=10
    )

    transaction.sign(sender_wallet)

    print("Tilimiko transaction created!")
    print("Amount:", transaction.amount)
    print("Signed:", transaction.signature is not None)
    print("Signature valid:", transaction.is_valid())
