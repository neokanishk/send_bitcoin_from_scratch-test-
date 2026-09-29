from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes # Often needed for signing later

# Generate the private key using the SECP256k1 curve
private_key = ec.generate_private_key(ec.SECP256K1())

# Derive the public key from the private key
public_key = private_key.public_key()



print("private " , private_key ) 
print("public" , public_key) 
print(0x80 , private_key)
print("ECDSA Keypair generated successfully.")
