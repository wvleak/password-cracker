import dict_hashing

hpass = "77459b9b941bcb4714d0c121313c900ecf30541d158eb2b9b178cdb8eca6457e"

def cracker():
    print("Hello! This is a SHA256 password cracker. \n")
    hashed_password = input("Input the hashed password you want to crack:\n")
    menu1 = input("What type of attack: 1.Bruteforce 2.Dictionary\n")
    if menu1 == "1":
        print("Algorithm is under construction...")
    elif menu1 == "2":
        menu = input("Choose the dictionary you want to use:\n1.Richelieu 2.Import...\n")

        if menu == "1":
            dictionary = dict_hashing.text_to_dict("richelieu.txt")

        elif menu == "2":
            dictionary = dict_hashing.hash_dict()

        try:
            print("The plain password is: " + dictionary[hashed_password])
        except:
            print("Password not found in the dictionary")

cracker()

