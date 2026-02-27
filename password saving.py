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
    parameters=perm_password_access.key()
#     open parameters list with loop name each with perm_password_access and then fill the parameters
#     then append it in list so now you will save a password with all that and after that encrypt it and save it.
