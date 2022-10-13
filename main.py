import random
import pandas as pd
import time


while True:
    string = 'Enter a number to select an option:\n1. Find password\n2. New password\n3. Exit\n\n->'

    option = int(input(string))

    if option == 1:
        app = input("\nEnter the name of the app: ").lower()

        df = pd.read_csv("data.csv", sep=" ")

        query = df.loc[ df["app"] == app ]

        if query.shape[0] > 0:
            Idx = [i for i in range(1, query.shape[0] - 1)]

            print(f"\nFound {query.shape[0]} possible matching passwords...\n")
            time.sleep(3)

            for i in query.itertuples():
                info = f"{i.Index + 1}. app_name: {i.app}\n   username: {i.username}\n   email: {i.email}\n   password: {i.password}\n"
                print(info)

            selection = int(input("Enter a number next to the password you need from the ones found and it will be copied to clipboard: "))
            password = pd.DataFrame([query.iloc[selection - 1, 3]])
            password.to_clipboard(index=False, header=False)
            print("\nPassword successfully copied to clipboard")
        
        else:
            print("No matching password found")

    elif option == 2:
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = lowercase.upper()
        numbers = "1234567890"
        symbols = "~`!@#$%^&*()_-+=\|]}[{'\";:/?.>,<"

        characters = lowercase + uppercase + numbers + symbols


        def generate_password():
            lower = False                
            upper = False
            num = False
            sym = False

            password = "".join(random.sample(characters, len(characters)))[:14]

            weak_password = True
            
            for i in password:
                if i in lowercase and lower == False:
                    lower = True
                
                elif i in uppercase and upper == False:
                    upper = True
                
                elif i in numbers and num == False:
                    num = True
                
                elif i in symbols and sym == False:
                    sym = True
                
                elif lower and upper and num and sym:
                    return password
            
            if weak_password:
                return generate_password()


        def save_password(password):
            site = input("Application: ")
            username = input("Username: ")
            email = input("Email: ")
            password = password

            with open("data.csv", "a") as file:
                file.writelines(f"\n{site} {username} {email} {password}")
                print("Password saved and copied to clipboard")


        password = generate_password()

        df = pd.DataFrame([password])
        df.to_clipboard(index=False, header=False)

        save_password(password)
    
    else:
        break