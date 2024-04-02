import hashlib
import time

class ProofOfWork:
    def __init__(self, blockchain):
        self.blockchain = blockchain
        self.difficulty = 4  # Difficulty of the PoW algorithm, adjustable.

    def proof_of_work(self, block):
        """
        Function that finds the nonce for the given block so that the hash
        of the block with the nonce satisfies the blockchain's difficulty criteria.
        """
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * self.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def add_block(self, block, proof):
        """
        Attempts to add a block to the blockchain after verifying its proof.
        """
        previous_hash = self.blockchain.last_block().hash if self.blockchain.chain else '0'
        if previous_hash != block.previous_hash:
            return False, "The block's previous hash must match the hash of the last block."

        if not self.valid_proof(block, proof):
            return False, "The proof of work is invalid."

        block.hash = proof
        self.blockchain.chain.append(block)
        return True, "Block added to the blockchain."

    def valid_proof(self, block, block_hash):
        """
        Validates the proof: Does hash(block + nonce) contain 4 leading zeroes?
        """
        return (block_hash.startswith('0' * self.difficulty) and block_hash == block.compute_hash())

    def validate_chain(self):
        """
        Validates the entire blockchain using the current proof of work rules.
        """
        return self.blockchain.is_chain_valid()
