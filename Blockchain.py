from Block import Block
from Transaction import Transaction, Coinbase


class Blockchain:
    def __init__(self):
		    public_key_of_me = "PUBLIC KEY OF ME"
        self.blocks = [Block("ZEvMflZDcwQJmarInnYi88px+6HZcv2Uoxw7+/JOOTg=", [Coinbase("public key")], 0)]

    def insert_block(self, block):
        if not isinstance(block, Block):
            return False
