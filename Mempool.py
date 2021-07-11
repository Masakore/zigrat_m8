from Transaction import Transaction

class Mempool:
    def __init__(self):
        self.tx = []

    def insert_transaction(self, tx):
        assert isinstance(tx, Transaction)
        assert tx.is_valid()
        self.tx.append(tx)