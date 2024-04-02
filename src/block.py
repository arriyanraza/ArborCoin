import time
from hashlib import sha256

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        """
        Constructor for the Block class.
        :param index: Unique ID of the block.
        :param transactions: List of transactions included in the block.
        :param timestamp: Time of block creation.
        :param previous_hash: Hash of the previous block in the chain.
        :param nonce: Nonce used for mining (Proof of Work).
        """
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        """
        Computes the SHA-256 hash of the block contents.
        :return: The hexadecimal hash of the block.
        """
        block_string = "{}{}{}{}{}".format(self.index, self.transactions, self.timestamp, self.previous_hash, self.nonce)
        return sha256(block_string.encode()).hexdigest()

    def print_details(self):
        """
        Prints the details of the block. Useful for debugging and logging.
        """
        print(f"Index: {self.index}")
        print(f"Timestamp: {self.timestamp}")
        print(f"Transactions: {self.transactions}")
        print(f"Previous Hash: {self.previous_hash}")
        print(f"Nonce: {self.nonce}")
        print(f"Hash: {self.hash}")
