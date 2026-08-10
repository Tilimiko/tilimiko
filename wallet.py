from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes


class Wallet:
    def __init__(self):
        self.private_key = ec.generate_private_key(ec.SECP256K1())
        self.public_key = self.private_key.public_key()

    def get_private_key(self):
        return self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

    def get_public_key(self):
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def sign(self, message):
        return self.private_key.sign(
            message.encode(),
            ec.ECDSA(hashes.SHA256())
        )


if __name__ == "__main__":
    wallet = Wallet()

    print("Tilimiko wallet created!")
    print("\nPUBLIC KEY:")
    print(wallet.get_public_key().decode())

    print("PRIVATE KEY:")
    print(wallet.get_private_key().decode())
