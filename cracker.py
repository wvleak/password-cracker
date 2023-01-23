import dict_hashing
import hashlib
from os import system, name
#todo clean the code

print(""" 
█░█ ▄▀█ █▀ █░█   █▀▀ █▀█ ▄▀█ █▀▀ █▄▀ █▀▀ █▀█   █░█ ▄█ ░ █▀█
█▀█ █▀█ ▄█ █▀█   █▄▄ █▀▄ █▀█ █▄▄ █░█ ██▄ █▀▄   ▀▄▀ ░█ ▄ █▄█

                    [𝕒𝕦𝕥𝕙𝕠𝕣: 𝕨𝕧𝕝𝕖𝕒𝕜]
""")

def cracker():
    print("Hello! This is a SHA256 password cracker. \n")

    menu1 = ""

    while menu1 != "1" and menu1 != "2":
        print(menu1)
        print("[1] Bruteforce\n[2] Dictionary\n[3] Description")
        menu1 = input("[+] Choose Number : ")
        if menu1 == "3":

            # for windows
 #           if name == 'nt':
 #               _ = system('cls')

            # for mac and linux(here, os.name is 'posix')
 #           else:
 #               _ = system('clear')


            print("[1] Bruteforce | Conduct a normal bruteforce attack with a wordlist.")
            print("[2] Dictionary | Convert a wordlist into a dictionary (key:hash, value:plain-text). New formed dictionaries can be saved into a txt file.\n")

            input("Press Enter to continue...")

    hashed_password = input("[*] Hash: ")
    print("\nChoose the hashing algorithm:")
    print("[1] MD5\n[2] SHA-1\n[3] SHA-256")

    while True:
        c = input("[+] Choose a number:")
        if c == "1" or c == "2" or c == "3":
            break

    hashtype = ""

    if c == "1":
        hashtype = "md5"
    elif c == "2":
        hashtype = "sha1"
    elif c == "3":
        hashtype = "sha256"


    if menu1 == "1": #todo put into dedicated function
        file = input("[*] Wordlist(path): ")
        with open(file, "r") as f:
            plain_password = ""
            text = f.read().splitlines()
            print("Cracking...")
            if hashtype == "md5":
                for word in text:
                    crypted = hashlib.md5(word.encode("utf-8")).hexdigest()
                    if crypted == hashed_password:
                        plain_password = word
                        print("The plain password is: " + plain_password)
                        break
                if plain_password == "":
                    print("Looped through all the wordlist")
                    print("Password not found.")

            elif hashtype == "sha1":
                for word in text:
                    crypted = hashlib.sha1(word.encode("utf-8")).hexdigest()
                    if crypted == hashed_password:
                        plain_password = word
                        print("The plain password is: " + plain_password)
                        break
                if not plain_password:
                    print("Looped through all the wordlist")
                    print("Password not found...")

            elif hashtype == "sha256":
                for word in text:
                    crypted = hashlib.sha256(word.encode("utf-8")).hexdigest()
                    if crypted == hashed_password:
                        plain_password = word
                        print("The plain password is: " + plain_password)
                        break
                if not plain_password:
                    print("Looped through all the wordlist")
                    print("Password not found...")

    elif menu1 == "2":





        print("\nChoose the dictionary:")
        print("[1] Richelieu\n[2] Saved passwords\n[3] Import new wordlist...")
        menu = input("[+] Choose a number: ")


        if menu == "1":
            dictionary = dict_hashing.text_to_dict("richelieu_"+hashtype+".txt")
        elif menu == "2":
            dictionary = dict_hashing.text_to_dict("saved_hashes_"+hashtype+".txt")
        elif menu == "3":
            dictionary = dict_hashing.hash_dict(hashtype)

        try:
            print("The plain password is: " + dictionary[hashed_password])
        except:
            print("Password not found in the dictionary")

cracker()

