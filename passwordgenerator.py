''' Build a Secure Password Generator'''
import random

special_characters = ['&', '#', '$', '!', '?', '"', '(', ')', '.']

alphabetic_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                                                                                                                          'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeric_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

new_password_create = "1"
login_list = "2"
find_password = "3"

menu_choices = [new_password_create, login_list, find_password]

password_vault = []


password_length = random.randint(11, 14)
if password_length == 11:
    min_alpha_length = 5
    min_special_length = 3
    min_numeric_length = 3
elif password_length == 12:
    min_alpha_length = 6
    min_special_length = 3
    min_numeric_length = 3
elif password_length == 13:
    min_alpha_length = 6
    min_special_length = 3
    min_numeric_length = 4
else:
    min_alpha_length = 6
    min_special_length = 4
    min_numeric_length = 4





def password_creation():
    password_list = []
    website = input("Enter the name of the website: ")
    def generate_password():
        password_length_count = 0
        alpha_length = 0
        special_length = 0
        numeric_length = 0
        while password_length_count < password_length:
            while alpha_length < min_alpha_length:
                password_list.append(alphabetic_characters[random.randint(0, len(alphabetic_characters) - 1)])
                alpha_length = alpha_length + 1
            while special_length < min_special_length:
                password_list.append(special_characters[random.randint(0, len(special_characters) - 1)])
                special_length = special_length + 1
            while numeric_length < min_numeric_length:
                password_list.append(numeric_characters[random.randint(0, len(numeric_characters) - 1)])
                numeric_length = numeric_length + 1
            password_length_count += 1
    def randomiser():
        random_count = 0
        while random_count < 10:
            for characters in password_list:
                password_list.remove(characters)
                password_list.insert(random.randint(0, len(password_list) - 1), characters)
                random_count = random_count + 1
    def stringpass():
        stringpassword = ""
        for each in password_list:
            stringpassword = stringpassword + password_list[password_list.index(each)]
        print(f"Your generated password is : {stringpassword}")
        password_vault.append([website.casefold(), stringpassword])

    def run_generate():
        generate_password()
        randomiser()
        stringpass()
    
    run_generate()
    


def main():
    while True:
        print("Select an option to continue")
        print(f"{new_password_create}. Generate New Password")
        print(f"{login_list}. See Vault")
        print(f"{find_password}. Search Login Details")

        choice = input("Select Option: ")
        if choice not in menu_choices:
            print("Invalid Choice")
            continue
        if choice == new_password_create:
            password_creation()
        elif choice == login_list:
            for logins in password_vault:
                print(f"Website : {password_vault[password_vault.index(logins)][0]}")
                print(f"Password : {password_vault[password_vault.index(logins)][1]}")
                print("    ")
        elif choice == find_password:
            found = False
            search = input("Enter the name of website to search login: ")
            for details in password_vault:
                if search.casefold() == password_vault[password_vault.index(details)][0]:
                    found = True
                    site = details
                    break
            if found == True:
                print(f"Website : {site[0]}")
                print(f"Password : {site[1]}")
            else:
                print("Login details not found")


if __name__ == "__main__":
    main()
