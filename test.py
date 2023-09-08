import hashlib


def password_hash(password):
    encoded = password.encode()
    encrypted = hashlib.sha256(encoded)
    
    return [encrypted.hexdigest(),encrypted]


print(password_hash("12345678")[0])