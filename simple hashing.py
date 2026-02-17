import hashlib
import os

modify=hashlib.sha3_512()

password=input("enter the top secret password")
modify.update(password.encode())
converted_words=modify.hexdigest()
try:
    parent='E:/'
    file_to_make='top_secret'
    path=os.path.join(parent,file_to_make)
    os.mkdir(path)
except FileNotFoundError as e:
    print('folder not found:', e)
except PermissionError as e:
    print('access denied:', e)
except Exception as e:
    print('something unexpected happened:', e)
save_file=open(f'{path}/hashed.txt','w+')
save_file.write(f'date-2026-03-15{converted_words}')
print(save_file.read())
save_file.close()

