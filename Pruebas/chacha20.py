# https://asecuritysite.com/encryption/salsa20
from Crypto.Cipher import Salsa20
import hashlib
from base64 import b64encode
from Crypto.Cipher import ChaCha20

def cifrarTest(plainText, secret):
    cipher = ChaCha20.new(key=secret.digest())
    ciphertext = cipher.encrypt(plainText)
    print("Plain text:\t",plainText)
    print("Key used:\t",b64encode(secret.digest()))
    return cipher, ciphertext

def descifrarTest(secret, ciphertext, cipher):
    cipher = ChaCha20.new(key=secret.digest(), nonce=cipher.nonce)
    plaintext = cipher.decrypt(ciphertext)
    print("Decrypted:\t",plaintext)

if __name__ == "__main__":
    plaintext = b'Hola mundo'
    key= b'Soy una llave secreta'
    secret = hashlib.sha256()
    secret.update(key)
    cipher, ciphertext = cifrarTest(plaintext,secret)
    descifrarTest(secret,ciphertext, cipher)

########################################3


# plaintext = b'Hola mindo'
# key= b'Soy una llave secreta'

# print("Plain text:\t",plaintext)
# print("Secret key:\t",key)

# secret = hashlib.sha256()

# secret.update(key)

# print("Key used:\t",b64encode(secret.digest()))

# cipher = ChaCha20.new(key=secret.digest())
# ciphertext = cipher.encrypt(plaintext)

# nonce = b64encode(cipher.nonce).decode('utf-8')
# ct = b64encode(ciphertext).decode('utf-8')
# print("\n---ChaCha20 Encrypt")
# print(" Nonce:",nonce)
# print(" Cipher:",ct)

# print("\n---ChaCha20 Decrypt")
# cipher = ChaCha20.new(key=secret.digest(), nonce=cipher.nonce)
# plaintext = cipher.decrypt(ciphertext)
# print(" Decrypted:\t",plaintext)