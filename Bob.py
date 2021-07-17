from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64

f = open('AlicePubKey.pem', 'r')
AlicPubKey = RSA.import_key(f.read())
f.close()

f = open('Message.pem', 'r')
message = f.read()
f.close()

f = open('Signature.pem', 'r')
signature = f.read()
signature = base64.b64decode(signature)
f.close()

print("Bob received message (", message, signature, ") from Alice.")
h = SHA256.new(message.encode('utf-8'))
try:
    pkcs1_15.new(AlicPubKey).verify(h, signature)
    print("The signature is valid")
except(ValueError, TypeError):
    print("The signature is not valid")
