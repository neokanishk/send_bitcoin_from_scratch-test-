import secrets
import hashlib

def generate_sha256_hash(input_string):
    # Encode the string to bytes, as hash functions require bytes as input
    input_bytes = input_string.encode('utf-8')
    
    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256(input_bytes)
    
    # Get the hexadecimal representation of the hash
    hex_digest = hash_object.hexdigest()
    
    return hex_digest
def ripemd160_hash(data_string):
  """
  Generates the RIPEMD-160 hash for a given string.

  Args:
    data_string: The input string to hash.

  Returns:
    The 40-character hexadecimal representation of the hash.
  """
  # Encode the string to bytes, which is required by hashlib
  data_bytes = data_string.encode('utf-8')
  
  # Create a new RIPEMD-160 hash object
  hasher = hashlib.new('ripemd160')
  
  # Update the hash object with the bytes
  hasher.update(data_bytes)
  
  # Return the hexadecimal digest
  return hasher.hexdigest()
def generate_bitcoin_key():
    # Generate 32 bytes (256 bits) of random data
    priv_key = secrets.token_hex(32)
    return priv_key
def getaddress(private_key):
	ecdsa_key = generate_sha256_hash(private_key)
	rip_key = ripemd160_hash(ecdsa_key)
	return rip_key 
# Example usage
private_key = generate_bitcoin_key()
print(f"Private Key (Hex): {private_key}")
getaddress(private_key)

