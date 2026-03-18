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


# if in future the main function breaks this is the old version it works perfectly.
# def main():
#     print("1. Create new vault")
#     print("2. Add passwords to existing vault")
#     print("3. View passwords")
#     choice = int(input("enter 1, 2 or 3: "))
#
#     if choice == 1:
#         path = input("enter folder name: ")
#         path1, key_file_path = create_new_file(path)
#     elif choice == 2 or choice == 3:
#         path1 = input("enter your vault file path: ")
#         key_file_path = input("enter your key file path: ")
#     else:
#         print("invalid choice")
#         return
#
#     if choice == 3:
#         c = open(key_file_path, 'rb')
#         key = c.read()
#         f = Fernet(key)
#         c.close()
#         a = open(path1, 'rb')
#         data = a.read()
#         a.close()
#         decrypted = f.decrypt(data)
#         passwords = json.loads(decrypted)
#         print("\n--- YOUR PASSWORDS ---")
#         for key, values in passwords.items():
#             print(f"{key}: {values}")
#         return
#
#     while True:
#         choice = int(input("enter 1 to save password 0 to quit: "))
#         if choice == 1:
#             path1, perm_password_access = saving_passwords(path1, key_file_path)
#             save_password_dict(path1, perm_password_access, key_file_path)
#         elif choice == 0:
#             break
#         else:
#             print("enter 1 or 0")
#
#
# main()