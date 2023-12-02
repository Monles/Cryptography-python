from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os
from Crypto.Util.Padding import unpad


def cbc_encrypt(plaintext, key, iv):
  cipher = AES.new(key, AES.MODE_CBC, iv)
  padded_plaintext = pad(plaintext, AES.block_size)
  ciphertext = iv + cipher.encrypt(padded_plaintext)
  return ciphertext


def cbc_decrypt(ciphertext, key, iv):
  cipher = AES.new(key, AES.MODE_CBC, iv)
  plaintext = cipher.decrypt(ciphertext[AES.block_size:])
  return unpad(plaintext, AES.block_size)


# Example usage:
key = os.urandom(16)  # 128-bit key
iv = os.urandom(16)  # 128-bit initialization vector (IV)

plaintext = b"Hello, CBC encryption!"
print("Original Text:", plaintext.decode('utf-8'))

# Encrypt
ciphertext = cbc_encrypt(plaintext, key, iv)
print("Encrypted Text:", ciphertext.hex())

# Decrypt
decrypted_text = cbc_decrypt(ciphertext, key, iv)
print("Decrypted Text:", decrypted_text.decode('utf-8'))

# Original Text: Hello, CBC encryption!
# Encrypted Text: cf029efe78217f0df7ae17f6607fd8ff65ecf1f13613c30956f16f894cf93aa0056c8bec016f71a8ec7f2defa147af84
# Decrypted Text: Hello, CBC encryption!