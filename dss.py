from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

private_key = RSA.generate(2048)
public_key = private_key.publickey()


message = b"This is the message to be signed"


h = SHA256.new(message)


signature = pkcs1_15.new(private_key).sign(h)

try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Signature verified")
except (ValueError, TypeError):
    print("Invalid signature")
