import os
import json

from cryptography.fernet import Fernet

def create_new_file(path):
    try:
        os.mkdir(path)
    except FileExistsError as e:
        print(e)
    except Exception as e:
        print(e)
    key = Fernet.generate_key()
    security=Fernet(key)
    file=input("Enter the name of the file")
    path1=os.path.join(path,file)
    password_vault_center={'password':[],'website,place,for where':[],'date':[],'importance':[]}
    json_converter=json.dumps(password_vault_center)
    a=open(path1,'wb')
    encrypted_password_vault_center=security.encrypt(json_converter.encode())
    a.write(encrypted_password_vault_center)
    a.close()
    key_file_name=input("enter name of the key file for encryption and decryption")
    key_file_path=os.path.join(path,key_file_name)
    b=open(key_file_path,'wb')
    b.write(key)
    b.close()
    return path1,key_file_path

def saving_passwords(path,key_file_path):
    c=open(key_file_path,'rb')
    key=c.read()
    f=Fernet(key)
    c.close()
    a=open(path,'rb')
    temp_password_access=a.read()
    a.close()
    original_password_manager=f.decrypt(temp_password_access)
    perm_password_access=json.loads(original_password_manager)
    parameters=perm_password_access.keys()

    try:
        for i in parameters:
            details=input(f'enter {i}')
            perm_password_access[i].append(details)
    except Exception as e:
        print("error in saving passwords block loop section", e)

    try:
        choice=int(input('enter 1 for saving password again 0 for finish'))
        if choice==1:
            path,updated_dict=saving_passwords(path,key_file_path)
            perm_password_access.extend(updated_dict)
        elif choice==0:
            pass
        else:
            print('enter either yes or no')

    except Exception as e:
        print(f'error on choice variable in saving passwords function',e)


    return path,perm_password_access

def save_password_dict(path,password_dictionary,key_file_path):
    c=open(key_file_path,'rb')
    key=c.read()
    f=Fernet(key)
    c.close()
    b = open(path, 'wb')
    final_password_lst = json.dumps(password_dictionary)
    encrypted_password_vault=f.encrypt(final_password_lst.encode())
    b.write(encrypted_password_vault)
    b.close()


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "config.txt")

    # NEW: optional one time folder override
    temp = input("press enter to use default folder or type a folder path for this session only: ").strip()
    if temp:
        config_path = os.path.join(temp, "config.txt")

    print("1. Create new vault")
    print("2. Add passwords to existing vault")
    print("3. View passwords")
    choice = int(input("enter 1, 2 or 3: "))

    if choice == 1:
        path = input("enter folder name: ")
        path1, key_file_path = create_new_file(path)
        with open(config_path, 'w') as config:
            config.write(path1 + "\n")
            config.write(key_file_path + "\n")
        print("paths saved to config.txt")

    elif choice == 2 or choice == 3:
        if os.path.exists(config_path):
            with open(config_path, 'r') as config:
                path1 = config.readline().strip()
                key_file_path = config.readline().strip()
        else:
            print("no config file found")
            create_config = input("do you want to create one? enter yes or no: ")
            if create_config.lower() == "yes":
                path1 = input("enter your vault file path: ")
                key_file_path = input("enter your key file path: ")
                with open(config_path, 'w') as config:
                    config.write(path1 + "\n")
                    config.write(key_file_path + "\n")
                print("config.txt created and paths saved")
            else:
                print("cannot proceed without paths")
                return
    else:
        print("invalid choice")
        return

    if choice == 3:
        c = open(key_file_path, 'rb')
        key = c.read()
        f = Fernet(key)
        c.close()
        a = open(path1, 'rb')
        data = a.read()
        a.close()
        decrypted = f.decrypt(data)
        passwords = json.loads(decrypted)
        print("\n--- YOUR PASSWORDS ---")
        for key, values in passwords.items():
            print(f"{key}: {values}")
        return

    while True:
        choice = int(input("enter 1 to save password 0 to quit: "))
        if choice == 1:
            path1, perm_password_access = saving_passwords(path1, key_file_path)
            save_password_dict(path1, perm_password_access, key_file_path)
        elif choice == 0:
            break
        else:
            print("enter 1 or 0")

main()
#finish2

