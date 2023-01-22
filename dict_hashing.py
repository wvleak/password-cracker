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


def text_to_dict(file):
    dict = {}
    with open(file, "r") as f:
        text = f.read().splitlines()
        for hash_password in text:
            hash = hash_password.split(":")[0]
            password = hash_password.split(":")[1]
            dict[hash] = password
    return dict



def hash_dict():

    file = input("Enter the path to the file :\n")

    export = input("Do you want to save the new file ? (Y/N) :\n")

    plist = file_to_array(file)
    hlist = password_hashing(plist)

    dict = {hlist[i]: plist[i] for i in range(len(plist))}
    #print(dict)

    if export == "Y":
        export_name = input("Name of the new file :\n")
        f = open(export_name+".txt","w")
        for key, value in dict.items():
            f.write('%s:%s\n' % (key, value))

    return dict




#password_list = file_to_array("common_passwords.txt")
#hashed_passwords_list = password_hashing(password_list)

#print(password_list)
#print(hashed_passwords_list)

#dictionary = hash_dict()

#print(dictionary) #todo save dict file
#text_to_dict("richelieu.txt")