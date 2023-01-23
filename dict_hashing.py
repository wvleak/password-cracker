import hashlib

def file_to_array(file):
    with open(file,"r") as f:
        passwords = f.read().splitlines()
    return passwords

def password_hashing(passwords, htype):
    hashed_password = []

    for password in passwords:
        if htype == "md5":
            hashed_password.append(hashlib.md5(password.encode("utf-8")).hexdigest())
        elif htype == "sha1":
            hashed_password.append(hashlib.sha1(password.encode("utf-8")).hexdigest())
        elif htype == "sha256":
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



def hash_dict(htype):
    export = ""
    file = input("Enter the path to the file :\n")

    while export != "Y" and export != "y" and export != "N" and export != "n":
        export = input("Do you want to save the dictionary ? (Y/N) :\n")

    plist = file_to_array(file)
    hlist = password_hashing(plist, htype)

    dict = {hlist[i]: plist[i] for i in range(len(plist))}
    #print(dict)

    if export == "Y" or export == "y":
        f = open("saved_hashes_"+htype+".txt","a")
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