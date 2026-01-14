from roles import *
from logins import check_login

def main():
    
    while True:
        role = input("Enter Role (admin / doctor / receptionist): ").strip().lower()
        password = input("Enter Password: ")

        # login check
        if check_login(role, password):
            print(f"\n Login successful as {role}")

            if role == "admin":
                admin()               # admin123                                  

            elif role == "doctor":
                doctor()             # doc123

            elif role == "receptionist":
                receptionist()      # recep123

            else:
                print("Unknown role!")

            break
        else:
            print("Invalid role or password. Try again.\n")


while True :
    print("...........Welcome to Hospital Management System ......")
    print("press 1 to continue ")
    print ("enter 2 for exit")
    choice = input("press 1 to continue or 2 to exit : ")
    if choice == '1':
        main()
    elif choice == '2':
        print("Thanksssss.....exiting...........")
        break
    else:
        print("invalid choice........")
    