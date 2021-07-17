from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64

f = open('AlicePrivKey.pem', 'r')
AlicePrivKey = RSA.import_key(f.read(), passphrase="!@#$")
f.close()

message = 'To be signed'
h = SHA256.new(message.encode('utf-8'))
signature = pkcs1_15.new(AlicePrivKey).sign(h)
print("Alice sent (", message, signature, ") to Bob.")

f = open('Message.pem', 'w')
f.write(message)
f.close()

f = open('Signature.pem', 'w')
f.write(base64.b64encode(signature).decode())
f.close()
