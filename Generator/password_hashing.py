import hashlib

def hash_pwd(pwd):
    hashed_password = hashlib.sha256(pwd.encode()).hexdigest()
    return hashed_password