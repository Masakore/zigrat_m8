class Transaction:
	def __init__(self, utxo, receiver_public_key, message, signature):
		self.utxo = utxo
		self.receiver_public_key = receiver_public_key
		self.message = message
		self.signature = signature
		assert is_valid()

	def get_hash(self):
		return "0"

class Coinbase:
	def __init__(self, receiver):
		self.receiver = receiver,
		self.message = 50 

	def get_hash(self):
		return "0"
