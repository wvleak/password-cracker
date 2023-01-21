import hashlib

def file_to_array(file):
    with open(file,"r") as f:
        passwords = f.read().splitlines()
    return passwords

def password_hashing(passwords):
    hashed_password = []
    for password in passwords:
        hashed_password.append(hashlib.sha256(password.encode("utf-8")).hexdigest())
    return hashed_password

def hash_dict(file):
    plist = file_to_array(file)
    hlist = password_hashing(plist)

    dict = {hlist[i]: plist[i] for i in range(len(plist))}
    return dict




#password_list = file_to_array("common_passwords.txt")
#hashed_passwords_list = password_hashing(password_list)

#print(password_list)
#print(hashed_passwords_list)

dictionary = hash_dict("common_passwords.txt")

print(dictionary) #todo save dict file
