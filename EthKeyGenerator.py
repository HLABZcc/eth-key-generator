from coincurve import PublicKey
from Crypto.Hash import keccak
import secrets

k = keccak.new(data=secrets.token_bytes(32), digest_bits=256)
private_key = k.digest()
print(f"private key: {private_key.hex()}")

public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
print(f"public key: {public_key.hex()}")

address = keccak.new(data=public_key, digest_bits=256).digest()[-20:]
print(f"eth addr: 0x{address.hex()}")
