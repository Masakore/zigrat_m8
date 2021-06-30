from inspect import signature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

private_key = rsa.generate_private_key(
	public_exponent=65537,
	key_size=4096,
	backend=default_backend()
)
pem = private_key.private_bytes(
	encoding=serialization.Encoding.PEM,
	format=serialization.PrivateFormat.PKCS8,
	encryption_algorithm=serialization.BestAvailableEncryption(b'password')
)
public_key = private_key.public_key()
public_pem = public_key.public_bytes(
	encoding=serialization.Encoding.PEM,
	format=serialization.PublicFormat.SubjectPublicKeyInfo
)
public_key_loaded = serialization.load_pem_public_key(public_pem, backend=default_backend())
private_key_loaded = serialization.load_pem_private_key(pem, backend=default_backend(), password=b"password")

# b binary
message = b"Hello World42" 
signature = private_key.sign(
	message,
	padding.PSS(
		mgf=padding.MGF1(hashes.SHA3_256()),
		salt_length=padding.PSS.MAX_LENGTH
	),
	hashes.SHA3_256()
)

# Introduction to Modern Cryptography
verify = public_key.verify(
	signature,
	message,
	padding.PSS(
		mgf=padding.MGF1(hashes.SHA3_256()),
		salt_length=padding.PSS.MAX_LENGTH
	),
	hashes.SHA3_256()
)

print(verify)
