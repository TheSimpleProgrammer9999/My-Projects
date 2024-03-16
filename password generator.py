def continueprocess():
    ask_save=input("want to save your password? y/n")
    if ask_save=="y":
        print("password sucessfully saved")
        with open("save passwords",'a') as file:
            file.write(ask_)
        
def encrypt_save():
    ask_save_encrypt=input("want to save your encrypted password? y/n")
    if ask_save_encrypt=="y":
        print("password sucessfully saved")
        with open("save encrypted passwords",'a') as fileE:
            fileE.write(encrypted_password+"\n")

while True:
    input_=input("what you want to do?(p to create password, e to create encrypted password)")
    if input_=="p":
        ask_=input("\nwrite your password down: ")
        if len(ask_)<5:
            print("\npassword is too short")
            continue
        elif len(ask_)==5:
            print("\npassword is ok")
            continueprocess()
        else:
            print("\npassword is strong")
            continueprocess()
    elif input_=="e":
        ask_encrypt=input("\nwrite your password down(we'll encrypt the result): ")
        if len(ask_encrypt)<5:
            print("\npassword is too short for encrypting")
            continue
        elif len(ask_encrypt)==5:
            print("\npassword is ok for encrypting")
            encrypted_password="*"*len(ask_encrypt)
            encrypt_save()
        else:
            print("\npassword is strong for encrypting")
            encrypted_password="*"*len(ask_encrypt)
            encrypt_save()
