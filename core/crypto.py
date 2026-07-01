from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def genkey():
	private_key = rsa.generate_private_key(
		public_exponent=65537,
		key_size=2048
	)

	public_key = private_key.public_key()

	return private_key, public_key

def serialize(pub):
	public_pem = pub.public_bytes(
	    encoding=serialization.Encoding.PEM,
	    format=serialization.PublicFormat.SubjectPublicKeyInfo
	)

	return public_pem

def deserialize(pem):
	public_key = serialization.load_pem_public_key(pem)
	return public_key

def encrypt(msg, pub):
	ciphertext = pub.encrypt(
		msg,
	    padding.OAEP(
	        mgf=padding.MGF1(algorithm=hashes.SHA256()),
	        algorithm=hashes.SHA256(),
	        label=None
	    )
	)

	return ciphertext

def decrypt(msg, priv):
	decrypted_message = priv.decrypt(
	    msg,
	    padding.OAEP(
	        mgf=padding.MGF1(algorithm=hashes.SHA256()),
	        algorithm=hashes.SHA256(),
	        label=None
	    )
	)

	return decrypted_message