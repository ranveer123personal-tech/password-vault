import os
import json


def create_new_file(path):
    try:
        os.mkdir(path)
    except FileExistsError as e:
        print(e)
    except Exception as e:
        print(e)
    file=input("Enter the name of the file")
    path1=os.path.join(path,file)
    password_vault_center={'password':[],'website,place,for where':[],'date':[],'importance':[]}
    a=open(path1,'w')
    a.write(json.dumps(password_vault_center))
    a.close()
    return path1

def saving_passwords(path):
    a=open(path,'r+')
    temp_password_access=a.read()
    a.close()
    perm_password_access=json.loads(temp_password_access)
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
            path,updated_dict=saving_passwords(path)
            perm_password_access.update(updated_dict)
        elif choice==0:
            pass
        else:
            print('enter either yes or no')

    except Exception as e:
        print(f'error on choice variable in saving passwords function',e)


    return path,perm_password_access

def save_password_dict(path,password_dictionary):
    b = open(path, 'r+')
    final_password_lst = json.dumps(password_dictionary)
    b.write(final_password_lst)
    b.close()


def temp_work():
    parent = r'E:\top_secret123'
    path_for_saving_passwords = create_new_file(parent)
    return path_for_saving_passwords
a=r"E:\top_secret123\password manager"
path,updated_dict=saving_passwords(a)
save_password_dict(path,updated_dict)

# now make a control center or whatever to link all of them and before that save in encrypted form and add decrypt method.

