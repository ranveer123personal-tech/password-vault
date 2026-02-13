import hashlib

converter=hashlib.sha256()
a=input("enter password")
converter.update(a.encode())
print(converter.digest())