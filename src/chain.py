from block import Block
import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain, known as the Genesis Block.
        This block has an index of 0, previous_hash of 0, and a valid hash.
        """
        genesis_block = Block(index=0, transactions=[], timestamp=time.time(), previous_hash="0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def add_block(self, block, proof):
        """
        Adds a new block to the chain after verification.
        Verification includes:
        - Checking that the proof is valid.
        - The previous_hash referred in the block and the hash of the latest block in the chain match.
        :param block: Block object to add.
        :param proof: The proof of work nonce that solves the given problem.
        """
        previous_hash = self.chain[-1].hash
        if previous_hash != block.previous_hash:
            return False  # The block is not referring to the latest block in the chain.

        if not self.is_valid_proof(block, proof):
            return False  # The provided proof is not valid.

        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self, block, block_hash):
        """
        Check if block_hash is a valid hash of the block and satisfies the difficulty criteria.
        This function can be expanded based on how you define the difficulty of your blockchain.
        """
        return (block_hash.startswith('0000') and block_hash == block.compute_hash())

    def last_block(self):
        """
        Returns the last block in the chain.
        """
        return self.chain[-1]

    def is_chain_valid(self):
        """
        Check if the blockchain is valid. It needs to check:
        - Each block's previous hash matches the hash of the previous block.
        - The block's hash is valid for each block.
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]

            if current.hash != current.compute_hash():
                return False  # The current block's hash is not correct.
            
            if current.previous_hash != previous.hash:
                return False  # The current block's previous_hash doesn't match the previous block's hash.

        return True
