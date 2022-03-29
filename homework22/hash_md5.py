import hashlib


def hash_md5(text):
    return hashlib.md5(str(text).encode('utf-8')).hexdigest()


print(hash_md5('Barinov'))
