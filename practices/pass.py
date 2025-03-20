import hashlib
password = input("password to hash: ")
hash_object = hashlib.sha256(password.encode())
print(hash_object.hexdigest())
